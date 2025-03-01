<script>
	import { scaleBand, scaleOrdinal } from "d3-scale";

	import { Html, LayerCake, Svg } from "layercake";
	import AxisY from "$components/missing/_components/AxisY.svelte";
	import AxisX from "$components/missing/_components/AxisX.svelte";
	import Bar from "$components/missing/_components/Bar.svelte";
	import Labels from "$components/missing/_components/Labels.svelte";

	import Scrolly from "$components/helpers/Scrolly.svelte";

	import {
		dataLookupForCharts,
		indexOfCopyToKpiAssociation
	} from "$data/preparedData.js";

	export let steps;
	export let index;
	export let title;

	let data;
	let value;
	let colors;

	const keyChart = "bar";
	const copyBodyType = "bar-chart";
	const renameValues = {
		"CERRADO POR FISCALIA / DELITO REFORMULADO": "CERRADO POR FISCALIA",
		"EXTRAVIADO - DISCAPACIDAD / ENFERMEDADES / TRASTORNOS":
			"EXTRAVIADO - DISCAPACIDAD"
	};

	// set x and y, keys
	const xKeyCat = "value";
	const yKeyCat = "cardinality";
	const zKeyCat = "value";

	// get cooked data which is a set
	const indexToKpi = indexOfCopyToKpiAssociation(copyBodyType, keyChart);
	const dataLookupForBarChart = dataLookupForCharts(keyChart);

	$: {
		data = dataLookupForBarChart.get(indexToKpi[index]);
		if (index == 5) {
			colors = Array.from({ length: data.length }, () => "#EB0F51f5");
		} else if (index == 6) {
			colors = Array.from({ length: data.length }, () => "#EB0F51CC");
		} else if (index == 9) {
			colors = [
				"#7fc97f",
				"#beaed4",
				"#fdc086",
				"#ffff99",
				"#386cb0",
				"#f0027f",
				"#bf5b17"
			];
		} else if (index == 10) {
			colors = [
				"#12B607cc",
				"#12B607cc",
				"#12B607cc",
				"#12B607cc",
				"#12B607cc",
				"#12B607cc",
				"#12B607cc",
				"#12B607cc",
				"#12B607cc",
				"#EB0F51CC",
				"#12B607cc",
				"#12B607cc"
			];
			data = data.map((obj) => {
				return Object.keys(obj).reduce((acc, key) => {
					acc[key] = renameValues[obj[key]] || obj[key];
					return acc;
				}, {});
			});
		}
		if (index != 5 && index != 6 && index != 9) {
			data = data.sort((a, b) => b.value - a.value);
		}
	}
</script>

<div class="charter">
	<div class="chart-container">
		<h5 class="chart-title">{title}</h5>
		<!-- {console.log("BarChart: value => ", value)} -->
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
				<AxisX />
				<AxisY tickMarks gridlines={false} />
				<Bar />
			</Svg>
			<Html>
				<Labels />
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
	@media (max-width: 600px) {
		.chart-container {
			margin-left: -40%;
			width: 140%;
		}
	}
</style>
