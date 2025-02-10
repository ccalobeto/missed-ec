<script>
	import { LayerCake, Svg } from "layercake";
	import Pie from "$components/missing/_components/Pie.svelte";

	import { dataLookupForCharts } from "$data/preparedData.js";

	export let step;
	let data;

	const innerRadius = 80;
	const outerRadius = 130;
	const padAngle = 0.05;

	// set x and y, keys
	const xKey = "percentage";
	const yKey = "cardinality";

	// get cooked data which is a set
	const dataLookupForDonutChart = dataLookupForCharts("donut");

	$: {
		if (step == 0) {
			data = dataLookupForDonutChart.get("tipology");
		}
		if (step == 1) {
			data = dataLookupForDonutChart.get("sex");
		}
	}

	// console.log("DonutChart: data => ", data);
</script>

<div class="chart-container">
	<LayerCake
		padding={{ top: 30, right: 0, bottom: 7, left: 0 }}
		x={xKey}
		y={yKey}
		xDomain={[0, 100]}
		xRange={({ height }) => [0, height / 2]}
		{data}
	>
		<Svg>
			<Pie {innerRadius} {outerRadius} {padAngle} />
		</Svg>
	</LayerCake>
</div>

<style>
	/*
    The wrapper div needs to have an explicit width and height in CSS.
    It can also be a flexbox child or CSS grid element.
    The point being it needs dimensions since the <LayerCake> element will
    expand to fill it.
  */
	.chart-container {
		width: 100%;
		height: 250px;
	}
</style>
