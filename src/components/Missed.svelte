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
		position: relative;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	:global(.text-blocks) {
		font-family: var(--serif);
		font-size: clamp(1rem, 2vw + 0.5rem, 2rem);
		width: clamp(300px, 80vw, 1200px);
		padding: min(0.2em, 5%);
	}

	:global(.chart-container) {
		position: sticky;
		transition: all 1s;
		height: 80vh;
		top: 4em;
	}
	:global(.scrolly-text-container) {
		width: clamp(300px, 80vw, 1200px);
	}
	:global(.spacer) {
		height: 20vh;
	}
	:global(.step) {
		border: 2px solid var(--color-gray-300);
		text-align: left;
		margin: 70vh 0;
		padding: 0 0 0 1.5rem;
		pointer-events: none;
	}
	:global(.step p) {
		font-family: var(--serif);
		width: min(400px, 80vw);
		padding: 0 2rem 0 0;
		font-size: clamp(0.5rem, 2vw + 0.5rem, 2rem);
		pointer-events: auto;
	}

	:global(.chart-title) {
		display: none;
		font-size: clamp(1rem, 1.5vw + 0.5rem, 2rem);
		background-color: aqua;
	}
</style>
