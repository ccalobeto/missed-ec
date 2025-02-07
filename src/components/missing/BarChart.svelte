<script>
	import { scaleBand } from "d3-scale";

	import { LayerCake, Svg } from "layercake";
	import AxisY from "$components/missing/_components/AxisY.svelte";
	import AxisX from "$components/missing/_components/AxisX.svelte";
	import Bar from "$components/missing/_components/Bar.svelte";

	import { dataLookupForCharts } from "$data/preparedData.js";

	export let step;
	let data;

	// set x and y, keys
	const xKeyCat = "percentage";
	const yKeyCat = "cardinality";

	// get cooked data which is a set
	const dataLookupForBarChart = dataLookupForCharts("bar");

	$: {
		if (step == 2) {
			data = dataLookupForBarChart.get("category");
			console.log("data => ", data);
		}
		if (step == 3) {
			data = dataLookupForBarChart.get("age_range");
		}
	}

	console.log("BarChart: dataLookupForBarChart => ", dataLookupForBarChart);
</script>

<!-- <h1>This is a bar Chart</h1> -->
<div class="scrolly-chart-container">
	{console.log("BarChart: step => ", step)}
	<div class="bar-container">
		<LayerCake
			padding={{ bottom: 20, left: 100 }}
			x={xKeyCat}
			y={yKeyCat}
			yScale={scaleBand().paddingInner(0.05)}
			xDomain={[0, null]}
			{data}
		>
			<Svg>
				<AxisX tickMarks baseline snapLabels />
				<AxisY tickMarks gridlines={false} />
				<Bar />
			</Svg>
		</LayerCake>
	</div>
</div>

<style>
	.bar-container {
		width: 80%;
		height: 250px;
		margin: 25px auto;
	}
</style>
