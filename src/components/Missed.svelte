<script>
	import DonutChart from "./missing/DonutChart.svelte";
	import BarChart from "./missing/BarChart.svelte";
	import ChoroplethMap from "./missing/ChoroplethMap.svelte";
	import { style } from "d3";

	export let copy;
</script>

<h2 class="title">{copy.title}</h2>
<p class="text-blocks">{@html copy.description}</p>

<div class="charts">
	<!-- {console.log("Charts: step => ", step)} -->
	{#each copy.body as item, index}
		<div class="type-{item['type']}">
			{#if item.type === "text"}
				<p class="text-blocks">{@html item.value}</p>
			{/if}
			{#if item.type === "donut-chart"}
				{@const steps = item.value.steps}
				<DonutChart {steps} />
			{/if}
			{#if item.type === "bar-chart"}
				{@const steps = item.value.steps}
				<BarChart {steps} />
			{/if}
			{#if item.type === "choropleth-map"}
				{@const steps = item.value.steps}
				<ChoroplethMap {steps} />
			{/if}
		</div>
	{/each}
</div>

<style>
	.title {
		max-width: 14em;
		margin: 0 auto;
		padding: 32px 0;
	}
</style>
