<script>
	import { quantize, interpolatePlasma } from "d3";

	import { LayerCake, Svg } from "layercake";
	import Pie from "$components/missing/_components/Pie.svelte";
	import Scrolly from "$components/helpers/Scrolly.svelte";

	import {
		dataLookupForCharts,
		indexOfCopyToKpiAssociation
	} from "$data/preparedData.js";

	export let steps;
	export let index;
	export let title;

	let value;
	let data;
	let colors;

	const innerRadius = 80;
	const outerRadius = 130;
	const padAngle = 0.05;

	// set x and y, keys
	const keyChart = "donut";
	const copyBodyType = "donut-chart";
	const xKey = "percentage";
	const yKey = "cardinality";

	// get cooked data which is a set
	const indexToKpi = indexOfCopyToKpiAssociation(copyBodyType, keyChart);
	const dataLookupForDonutChart = dataLookupForCharts(keyChart);

	$: {
		data = dataLookupForDonutChart.get(indexToKpi[index]);
		colors = ["#8ECEFD", "#F88B9D"];
	}
</script>

<div id="donut-chart">
	<div class="chart-container">
		<h5 class="chart-title">{title}</h5>
		<LayerCake
			padding={{ top: 30, right: 0, bottom: 7, left: 0 }}
			x={xKey}
			y={yKey}
			xDomain={[0, 100]}
			xRange={({ height }) => [0, height / 2]}
			{data}
		>
			<Svg>
				<Pie {innerRadius} {outerRadius} {padAngle} {colors} />
			</Svg>
		</LayerCake>
	</div>
	<div class="spacer"></div>
	<div class="scrolly-text-container">
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
	#donut-chart {
		padding-top: 30px;
		padding-bottom: 30px;
	}
</style>
