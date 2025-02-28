<script>
	import DonutChart from "./missing/DonutChart.svelte";
	import BarChart from "./missing/BarChart.svelte";
	import ChoroplethMap from "./missing/ChoroplethMap.svelte";

	export let copy;
</script>

<div class="charts">
	<!-- {console.log("Charts: step => ", step)} -->
	{#each copy.body as item, index}
		<div class="type-{item['type']}">
			{#if item.type === "text"}
				<p class="text-blocks">{@html item.value}</p>
			{/if}
			{#if item.type === "donut-chart"}
				{@const steps = item.value.steps}
				<DonutChart {steps} {index} />
			{/if}
			{#if item.type === "bar-chart"}
				{@const steps = item.value.steps}
				<BarChart {steps} {index} />
			{/if}
			{#if item.type === "choropleth-map"}
				{@const steps = item.value.steps}
				<ChoroplethMap {steps} {index} />
			{/if}
		</div>
	{/each}
</div>

<style>
	.text-blocks {
		font-family: var(--serif);
		font-size: var(--20px);
		max-width: 600px;
		margin-left: auto;
		margin-right: auto;
	}
</style>
