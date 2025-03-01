<!--
  @component
  Generates HTML text labels for a nested data structure. It places the label near the y-value of the highest x-valued data point. This is useful for labeling the final point in a multi-series line chart, for example. It expects your data to be an array of objects where each has `values` field that is an array of data objects. It uses the `z` field accessor to pull the text label.
 -->
<script>
	import { getContext } from "svelte";
	import { max } from "d3-array";

	const { data, x, y, xScale, yScale, xRange, yRange, z, xGet, yGet } =
		getContext("LayerCake");

	/* --------------------------------------------
	 * Title case the first letter
	 */
	// const cap = (val) => val.replace(/^\w/, (d) => d.toUpperCase());

	/* --------------------------------------------
	 * Put the label on top of the bar
	 */

	const barHeight = $yScale.bandwidth();

	$: left = (values) => $xGet(values) / Math.max(...$xRange);
	$: top = (values) => ($yGet(values) + barHeight / 2) / Math.max(...$yRange);
</script>

{#each $data as group}
	<div
		class="label"
		style="left:{left(group) * 100}%; top:{top(group) * 100}%;"
	>
		{$x(group)}
	</div>
{/each}

<style>
	.label {
		position: absolute;
		transform: translate(10%, -100%) translateY(15px);
		font-size: 11px;
	}
</style>
