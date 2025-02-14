<script>
	import DonutChart from "./missing/DonutChart.svelte";
	import BarChart from "./missing/BarChart.svelte";
	import ChoroplethMap from "./missing/ChoroplethMap.svelte";
	import { style } from "d3";

	export let copy;
</script>

<section>
	<h1>{copy.title}</h1>
	<p>{@html copy.description}</p>
	<img src="missing-child.jpg" alt="" />
</section>

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
	section {
		padding: 5px;
		margin: 5px;
		box-sizing: border-box;
	}
	section h1 {
		font-family: var(--serif);
		font-weight: 300;
		font-size: var(--36px);
		text-align: center;
	}

	section p {
		font-size: var(--14px);
		font-style: italic;
		text-align: center;
		max-width: 500px;
		margin-left: auto;
		margin-right: auto;
	}

	section img {
		aspect-ratio: 1;
		margin: auto;
	}

	.text-blocks {
		font-family: var(--serif);
		font-size: var(--20px);
		max-width: 600px;
		margin-left: auto;
		margin-right: auto;
	}
</style>
