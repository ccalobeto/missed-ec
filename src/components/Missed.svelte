<script>
	import DonutChart from "./missing/DonutChart.svelte";
	import BarChart from "./missing/BarChart.svelte";
	import ChoroplethMap from "./missing/ChoroplethMap.svelte";

	export let copy;
</script>

<div class="charts-container">
	<!-- {console.log("Charts: step => ", step)} -->
	{#each copy.body as item, index}
		<div class="type-{item['type']}">
			{#if item.type === "text"}
				<p class="text-blocks">{@html item.value}</p>
			{/if}
			{#if item.type === "donut-chart"}
				{@const steps = item.value.steps}
				{@const title = item.title}
				<DonutChart {steps} {index} {title} />
			{/if}
			{#if item.type === "bar-chart"}
				{@const steps = item.value.steps}
				{@const title = item.title}
				<BarChart {steps} {index} {title} />
			{/if}
			{#if item.type === "choropleth-map"}
				{@const steps = item.value.steps}
				{@const title = item.title}
				<ChoroplethMap {steps} {index} {title} />
			{/if}
		</div>
	{/each}
</div>

<style>
	.charts-container {
		border: 2px solid red;
		display: flex;
		flex-direction: column;
		align-items: center;
		position: relative;
	}

	:global(.chart-title) {
		display: inline;
	}
	:global(.text-blocks) {
		border: 2px solid black;
		font-family: var(--serif);
		font-size: clamp(1rem, 2vw + 0.5rem, 2rem);
		width: clamp(300px, 80vw, 1200px);
		padding: min(1em, 5%);
	}

	:global(.chart-container) {
		border: 2px dashed blue;
		width: clamp(300px, 80vw, 1200px);
		height: 80vh;
		position: sticky;
		top: 4em;
		justify-items: center;
	}
	:global(.scrolly-text-container) {
		border: 2px dashed green;
		position: relative;
	}
	:global(.spacer) {
		border: 2px dashed orange;
		height: 60vh;
	}
	:global(.step) {
		border: 2px solid var(--color-gray-300);
		text-align: left;
		width: 350px;
		margin: 70vh 0;
		padding: 0 0 0 1.5rem;
		pointer-events: none;
	}
	:global(.step p) {
		font-family: var(--serif);
		padding: 0 2rem 0 0;
		font-size: clamp(0.5rem, 2vw + 0.5rem, 2rem);
		pointer-events: auto;
	}
</style>
