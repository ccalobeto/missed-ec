<!--
  @component
  Generates an SVG radar chart.
 -->
<script lang="ts">
	import { getContext } from "svelte";
	import { quantize, interpolatePlasma, pie, arc } from "d3";

	const { data, width, height, x, y } = getContext("LayerCake");

	/**  @type {String} [fill='#f0c'] The radar's fill color. This is technically optional because it comes with a default value but you'll likely want to replace it with your own color. */
	export let fill = "#f0c";

	/**  @type {String} [stroke='#f0c'] The radar's stroke color. This is technically optional because it comes with a default value but you'll likely want to replace it with your own color. */
	export let stroke = "#636363";

	/**  @type {Number} [stroke=2] The radar's stroke color. */
	export let strokeWidth = 2;

	/**  @type {Number} [fillOpacity=0.5] The radar's fill opacity. */
	export let fillOpacity = 0.5;

	/**  @type {Number} [r=4.5] Each circle's radius. */
	export let r = 4.5;

	/**  @type {String} [circleFill="#f0c"] Each circle's fill color. This is technically optional because it comes with a default value but you'll likely want to replace it with your own color. */
	export let circleFill = "#f0c";

	/**  @type {String} [circleStroke="#fff"] Each circle's stroke color. This is technically optional because it comes with a default value but you'll likely want to replace it with your own color. */
	export let circleStroke = "#fff";

	/**  @type {Number} [circleStrokeWidth=1] Each circle's stroke width. */
	export let circleStrokeWidth = 1;

	export let percent = true;

	/**  @type {Number} [innerRadius=125] Each inner circle's radius. */
	export let innerRadius = 125;

	/**  @type {Number} [outerRadius=175] Each outer circle's radius. */
	export let outerRadius = Math.min(width, height) * 0.5 - 60;

	/**  @type {Number} [padAngle=0.312] Each outer circle's radius. */
	export let padAngle = 0.312;

	const labelPosition = 0.4; // the position of the label offset from center
	const labelRadius = innerRadius * labelPosition + outerRadius * 0.6; //
	const fontSize = 13; // the font size of the x and y valuescenter radius of labels

	// generate Data for pie
	$: wedges = pie().padAngle(padAngle).sort(null).value($x);

	$: pieArcs = wedges($data);

	$: arcPath = (arc() as any).innerRadius(innerRadius).outerRadius(outerRadius);

	$: colors = quantize((t) => interpolatePlasma(t * 0.7 + 0.3), $data.length);

	$: arcLabel = (arc() as any)
		.innerRadius(labelRadius)
		.outerRadius(labelRadius);

	console.log("Pie: pieArcs => ", pieArcs);
</script>

<g transform="translate({$width / 2}, {$height / 2})">
	{#each pieArcs as pieArc, i}
		{console.log("Pie: row => ", pieArc.data)}
		{console.log("Pie: x => ", $x(pieArc.data))}
		<!-- Draw a the paths -->
		<path
			class="path-line"
			d={arcPath(pieArc)}
			{stroke}
			stroke-width={strokeWidth}
			fill={colors[i]}
			fill-opacity={fillOpacity}
		></path>

		<!-- Draw the labels -->
		<g text-anchor="middle" transform="translate({arcLabel.centroid(pieArc)})">
			<text font-size={fontSize}>
				<tspan font-weight="bold">{$y(pieArc.data)}</tspan>
				<tspan x="0" dy="1.1em"
					>{percent
						? `${$x(pieArc.data).toFixed(2)}%`
						: $x(pieArc.data).toLocaleString("en-US")}</tspan
				>
			</text>
		</g>
	{/each}
</g>

<style>
	.path-line {
		stroke-linejoin: round;
		stroke-linecap: round;
	}
</style>
