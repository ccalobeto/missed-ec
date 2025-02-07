<script>
	import { LayerCake, Svg, Html } from "layercake";
	import { scaleQuantize } from "d3-scale";
	import { feature } from "topojson-client";
	import { geoIdentity } from "d3-geo";
	import { format } from "d3-format";

	import MapSvg from "$components/missing/_components/Map.svg.svelte";
	import Tooltip from "$components/missing/_components/Tooltip.html.svelte";

	import { stateData } from "$data/preparedData.js";
	import ec from "$data/support/ecuador-tm-50k.json";

	/* map plot  */
	const colorKey = "myValue";

	/* --------------------------------------------
	 * Create lookups to more easily join our data
	 * `dataJoinKey` is the name of the field in the data
	 * `mapJoinKey` is the name of the field in the map file
	 */
	const dataJoinKey = "name";
	const mapJoinKey = "name";
	const dataLookup = new Map();

	const geojson = feature(ec, ec.objects.level3);
	const projection = geoIdentity;

	stateData().forEach((d) => {
		if (d !== null) {
			dataLookup.set(d[dataJoinKey], d);
		}
	});

	let evt = null;
	let hideTooltip = true;

	// Create a flat array of objects that LayerCake can use to measure
	// extents for the color scale
	const flatData = geojson.features.map((d) => d.properties) || [];

	const colors = ["#ffdecc", "#ffc09c", "#ffa06b", "#ff7a33"];

	const addCommas = format(",");
</script>

<h1>This is a choropleth map</h1>

<div class="map-container">
	<LayerCake
		data={geojson}
		z={(d) => dataLookup.get(d[mapJoinKey])[colorKey]}
		zScale={scaleQuantize()}
		zRange={colors}
		{flatData}
	>
		<Svg>
			<MapSvg
				{projection}
				on:mousemove={(event) => (evt = hideTooltip = event)}
				on:mouseout={() => (hideTooltip = true)}
			/>
		</Svg>

		<Html pointerEvents={false}>
			{#if hideTooltip !== true}
				<Tooltip {evt} let:detail>
					<!-- For the tooltip, do another data join because the hover event only has the data from the geography data -->
					{@const tooltipData = {
						...detail.props,
						...dataLookup.get(detail.props[mapJoinKey])
					}}
					{#each Object.entries(tooltipData) as [key, value]}
						{@const keyCapitalized = key.replace(/^\w/, (d) => d.toUpperCase())}
						<div class="row">
							<span>{keyCapitalized}:</span>
							{typeof value === "number" ? addCommas(value) : value}
						</div>
					{/each}
				</Tooltip>
			{/if}
		</Html>
	</LayerCake>
</div>

<style>
	.map-container {
		width: 80%;
		height: 250px;
		margin: 25px auto;
	}
</style>
