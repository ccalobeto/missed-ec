<script>
	import { scaleBand } from "d3-scale";

	import { LayerCake, Svg } from "layercake";
	import AxisY from "$components/missing/_components/AxisY.svelte";
	import AxisX from "$components/missing/_components/AxisX.svelte";
	import Bar from "$components/missing/_components/Bar.svelte";

	import Scrolly from "$components/helpers/Scrolly.svelte";
	import { dataLookupForCharts } from "$data/preparedData.js";

	export let item;
	let value;

	// set x and y, keys
	const xKeyCat = "percentage";
	const yKeyCat = "cardinality";

	// storytelling notes
	const scrollySteps = item.value.steps;

	// get cooked data which is a set
	const dataLookupForBarChart = dataLookupForCharts("bar");

	console.log("dataLookupForBarChart => ", dataLookupForBarChart);
</script>

<h1>This is a bar Chart</h1>
<div id="bar-chart">
	<div class="scrolly-chart-container">
		<Scrolly bind:value>
			<!-- dataLookupForBarChart.entries() is a map iterator -->
			{#each dataLookupForBarChart.entries() as [k, v], i}
				{@const active = value === i}
				<div class="bar-container" class:active>
					<LayerCake
						padding={{ bottom: 20, left: 100 }}
						x={xKeyCat}
						y={yKeyCat}
						yScale={scaleBand().paddingInner(0.05)}
						xDomain={[0, null]}
						data={v}
					>
						<Svg>
							<AxisX tickMarks baseline snapLabels />
							<AxisY tickMarks gridlines={false} />
							<Bar />
						</Svg>
					</LayerCake>
				</div>
			{/each}
		</Scrolly>
	</div>
	<div class="spacer"></div>
	<div class="scrolly-text-container">
		<Scrolly bind:value>
			{#each scrollySteps as step, i}
				{@const active = value === i}
				<div class="step" class:active>
					<div class="step-text">{@html step.value}</div>
					{console.log("value =>", value)}
				</div>
			{/each}
		</Scrolly>
	</div>
</div>

<style>
	#bar-chart {
		padding-top: 30px;
		padding-bottom: 30px;
	}
	.bar-container {
		width: 80%;
		height: 250px;
		margin: 25px auto;
	}

	.spacer {
		height: 75vh;
	}

	.step {
		height: 80vh;
		background: var(--color-gray-300);
		text-align: center;
	}
</style>
