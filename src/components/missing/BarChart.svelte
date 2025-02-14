<script>
	import { scaleBand } from "d3-scale";

	import { LayerCake, Svg } from "layercake";
	import AxisY from "$components/missing/_components/AxisY.svelte";
	import AxisX from "$components/missing/_components/AxisX.svelte";
	import Bar from "$components/missing/_components/Bar.svelte";

	import Scrolly from "$components/helpers/Scrolly.svelte";

	import { dataLookupForCharts } from "$data/preparedData.js";

	export let steps;
	let data;
	let value;

	// set x and y, keys
	const xKeyCat = "percentage";
	const yKeyCat = "cardinality";

	// get cooked data which is a set
	const dataLookupForBarChart = dataLookupForCharts("bar");

	$: {
		if (value == 0) {
			data = dataLookupForBarChart.get("category");
		}
		if (value == 1) {
			data = dataLookupForBarChart.get("age_range");
		}
	}
</script>

<div id="bar-chart">
	<div class="chart-container">
		<!-- {console.log("BarChart: step => ", step)} -->
		<div class="chart-container">
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
		width: 80%;
		height: 250px;
		display: block;
		margin-left: auto;
		margin-right: auto;
		position: sticky;
		top: 4em;
	}

	#bar-chart {
		padding-top: 30px;
		padding-bottom: 30px;
	}

	.scrolly-text-container {
		position: relative;
		z-index: 5;
	}
	.spacer {
		height: 75vh;
	}
	.step {
		text-align: left;
		z-index: 1000;
		width: 350px;
		margin: 60vh 0;
		padding: 0 0 0 1.5rem;
		pointer-events: none;
	}
	.step p {
		font-family: var(--serif);
		padding: 0 2rem 0 0;
		font-size: var(--32px);
		pointer-events: auto;
		position: relative;
	}
</style>
