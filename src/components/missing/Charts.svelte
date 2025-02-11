<script>
	import DonutChart from "./DonutChart.svelte";
	import BarChart from "./BarChart.svelte";
	import ChoroplethMap from "./ChoroplethMap.svelte";

	export let step;
	export let scrollyTeller;
</script>

<div class="charts">
	<!-- {console.log("Charts: step => ", step)} -->
	{#each scrollyTeller as item, index}
		<div class="type-{item['type']}">
			{#if item.type === "donut-chart"}
				<DonutChart {step} />
			{/if}
			{#if item.type === "bar-chart" && step === index}
				<BarChart {step} />
			{/if}
			{#if item.type === "choropleth-map" && step === index}
				<ChoroplethMap {step} />
			{/if}
		</div>
	{/each}
</div>
