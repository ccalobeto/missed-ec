<script>
	import { getContext } from "svelte";
	import { scaleQuantize } from "d3-scale";
	import { feature } from "topojson-client";
	import { geoIdentity } from "d3-geo";
	import { format } from "d3-format";

	import { LayerCake, Svg, Html } from "layercake";
	import MapSvg from "$components/missing/_components/Map.svg.svelte";
	import Scrolly from "$components/helpers/Scrolly.svelte";
	import Tooltip from "$components/missing/_components/Tooltip.html.svelte";

	import {
		dataLookupForCharts,
		indexOfCopyToKpiAssociation
	} from "$data/preparedData.js";
	import ec from "$data/support/ecuador-tm-50k.json";

	export let steps;
	export let index;
	export let title;

	let data;
	let value;

	/* --------------------------------------------
	 * Create lookups to more easily join our data
	 * `dataJoinKey` is the name of the field in the data
	 * `mapJoinKey` is the name of the field in the map file
	 */
	const dataJoinKey = "id";
	const mapJoinKey = "id";
	const colorKey = "value";
	const dataLookup = new Map();
	const keyChart = "choropleth";
	const copyBodyType = "choropleth-map";

	const geojson = feature(ec, ec.objects.level3);
	const projection = geoIdentity;

	const indexToKpi = indexOfCopyToKpiAssociation(copyBodyType, keyChart);
	const dataLookupForMapChart = dataLookupForCharts(keyChart);

	$: {
		data = dataLookupForMapChart.get(indexToKpi[index]);
		data.forEach((d) => {
			if (d !== null) {
				dataLookup.set(d[dataJoinKey], d);
			}
		});
	}

	let evt = null;
	let hideTooltip = true;

	// Create a flat array of objects that LayerCake can use to measure
	// extents for the color scale
	const flatData = geojson.features.map((d) => d.properties) || [];

	const colors = ["#ffdecc", "#ffc09c", "#ffa06b", "#ff7a33"];

	const addCommas = format(",");
</script>

<div id="choropleth-chart">
	<div class="chart-container">
		<h5 class="chart-title">{title}</h5>
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
							{@const keyCapitalized = key.replace(/^\w/, (d) =>
								d.toUpperCase()
							)}
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
	<div class="spacer"></div>
	<div class="scrolly-text-container">
		<!-- {console.log("DonutChart: scrollyValue => ", value)} -->
		<Scrolly bind:value>
			{#each steps as step, i}
				<div class="step" class:active={value === i}>
					<p>{@html step}</p>
				</div>
			{/each}
		</Scrolly>
	</div>
</div>

<style>
	.chart-container {
		z-index: 5;
	}
</style>
