<script>
	import { quantize, interpolatePlasma } from "d3";

	import { LayerCake, Svg } from "layercake";
	import Pie from "$components/missing/_components/Pie.svelte";
	import Scrolly from "$components/helpers/Scrolly.svelte";

	import { dataLookupForCharts } from "$data/preparedData.js";

	export let steps;
	export let index;
	let value;
	let data;
	let colors;

	const innerRadius = 80;
	const outerRadius = 130;
	const padAngle = 0.05;

	// set x and y, keys
	const xKey = "percentage";
	const yKey = "cardinality";

	// get cooked data which is a set
	const dataLookupForDonutChart = dataLookupForCharts("donut");

	$: {
		if (index == 7) {
			data = dataLookupForDonutChart.get("sex");
			colors = ["#8ECEFD", "#F88B9D"];
		} else if (index == 9) {
			data = dataLookupForDonutChart.get("tipology");
			colors = ["#8f0da4", "#ea7457", "#f0f921"];
		}
	}

	$: console.log(
		"DonutChart: total => ",
		data.map((el) => el.value).reduce((a, b) => a + b, 0)
	);
</script>

<div id="donut-chart">
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
				<Pie {innerRadius} {outerRadius} {padAngle} {colors} />
			</Svg>
		</LayerCake>
	</div>
	<div class="spacer"></div>
	<div class="scrolly-text-container">
		{console.log("DonutChart: scrollyValue => ", value)}
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
	/*
    The wrapper div needs to have an explicit width and height in CSS.
    It can also be a flexbox child or CSS grid element.
    The point being it needs dimensions since the <LayerCake> element will
    expand to fill it.
  */
	.chart-container {
		width: 100%;
		height: 250px;
		display: block;
		margin-left: auto;
		margin-right: auto;
		position: sticky;
		top: 4em;
	}
	#donut-chart {
		padding-top: 30px;
		padding-bottom: 30px;
	}

	.scrolly-text-container {
		position: relative;
		z-index: 1;
	}
	.spacer {
		height: 75vh;
	}
	.step {
		text-align: left;
		width: 350px;
		margin: 60vh 0;
		padding: 0 0 0 1.5rem;
		pointer-events: none;
	}
	.step p {
		font-family: var(--serif);
		padding: 0 2rem 0 0;
		font-size: var(--28px);
		pointer-events: auto;
		position: relative;
	}
</style>
