<script>
	import { scaleBand, scaleOrdinal } from "d3-scale";

	import { LayerCake, Svg } from "layercake";
	import AxisY from "$components/missing/_components/AxisY.svelte";
	import AxisX from "$components/missing/_components/AxisX.svelte";
	import Bar from "$components/missing/_components/Bar.svelte";

	import Scrolly from "$components/helpers/Scrolly.svelte";

	import {
		dataLookupForCharts,
		indexOfCopyToKpiAssociation
	} from "$data/preparedData.js";

	export let steps;
	export let index;

	let data;
	let value;
	let colors;

	const currentValue = "2024";
	const currentColor = "#339900";
	const defaultColor = "#00bbff";
	const keyChart = "bar";
	const copyBodyType = "bar-chart";

	// set x and y, keys
	const xKeyCat = "value";
	const yKeyCat = "cardinality";
	const zKeyCat = "value";

	// get cooked data which is a set
	const indexToKpi = indexOfCopyToKpiAssociation(copyBodyType, keyChart);
	const dataLookupForBarChart = dataLookupForCharts(keyChart);

	$: {
		data = dataLookupForBarChart.get(indexToKpi[index]);
		if (index == 6) {
			colors = Array.from({ length: data.length }, () => "#c994c7");
		} else if (index == 7) {
			colors = Array.from({ length: data.length }, () => "#df65b0");
		} else if (index == 10) {
			colors = [
				"#7fc97f",
				"#beaed4",
				"#fdc086",
				"#ffff99",
				"#386cb0",
				"#f0027f",
				"#bf5b17"
			];
		} else if (index == 11) {
			colors = [
				"#c994c7",
				"#df65b0",
				"#e7298a",
				"#ce1256",
				"#91003f",
				"#d4b9da",
				"#f1eef6"
			];
		}
		if (index != 6 && index != 7 && index != 10) {
			data = data.sort((a, b) => b.value - a.value);
		}
	}
</script>

<div id="bar-chart">
	<div class="chart-container">
		<!-- {console.log("BarChart: value => ", value)} -->
		<div class="chart-container">
			<LayerCake
				padding={{ bottom: 20, left: 250 }}
				x={xKeyCat}
				y={yKeyCat}
				z={zKeyCat}
				yScale={scaleBand().paddingInner(0.05)}
				xDomain={[0, null]}
				yDomainSort={false}
				zRange={colors}
				zScale={scaleOrdinal()}
				{data}
			>
				<Svg>
					<AxisX tickMarks baseline snapLabels gridlines={false} />
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
