<script>
	import { LayerCake, Svg } from "layercake";
	import Pie from "$components/missing/_components/Pie.svelte";
	import Scrolly from "$components/helpers/Scrolly.svelte";

	import { dataLookupForCharts } from "$data/preparedData.js";

	export let steps;
	let value;
	let data;

	console.log("DonutChart: steps => ", steps);

	const innerRadius = 80;
	const outerRadius = 130;
	const padAngle = 0.05;

	// set x and y, keys
	const xKey = "percentage";
	const yKey = "cardinality";

	// get cooked data which is a set
	const dataLookupForDonutChart = dataLookupForCharts("donut");

	$: {
		if (value == 0) {
			data = dataLookupForDonutChart.get("tipology");
		}
		if (value == 1) {
			data = dataLookupForDonutChart.get("sex");
		}
	}

	console.log("DonutChart: value => ", value);
</script>

<div id="donut-chart">
	<div class="chart-container">
		<!-- {console.log("DonutChart: value => ", value)} -->
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
	<div class="spacer"></div>
	<div class="scrolly-text-container">
		<!-- {console.log("DonutChart: scrollyValue => ", value)} -->
		<Scrolly bind:value>
			{#each steps as step, i}
				<div class="step" class:active={value === i}>
					<div class="step-text">{@html step}</div>
				</div>
			{/each}
		</Scrolly>
	</div>
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
	#donut-chart {
		padding-top: 30px;
		padding-bottom: 30px;
	}

	.scrolly-text-container {
		position: relative;
		z-index: 5;
	}
	.step {
		height: 80vh;
		background: none;
		text-align: center;
		width: 30%;
		margin-left: auto;
		margin-right: auto;
	}

	.chart-container {
		display: block;
		margin-left: auto;
		margin-right: auto;
		position: sticky;
		top: 4em;
	}

	.step-text {
		background-color: #333;
		padding: 1rem;
	}
</style>
