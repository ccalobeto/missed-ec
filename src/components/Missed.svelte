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

	:global(.scrolly-text-container) {
		position: relative;
		z-index: 5;
	}
	:global(.spacer) {
		height: 75vh;
	}
	:global(.step) {
		text-align: left;
		width: 350px;
		margin: 60vh 0;
		padding: 0 0 0 1.5rem;
		pointer-events: none;
	}
	:global(.step p) {
		font-family: var(--serif);
		padding: 0 2rem 0 0;
		font-size: var(--32px);
		pointer-events: auto;
		position: relative;
	}

	@media (min-width: 1200px) {
		.step:last-of-type {
			font-size: 4.5rem;
		}
	}

	@media (max-width: 900px) {
		:global(.chart-container) {
			flex-direction: column;
			gap: 0;
			align-items: center;
			padding: 0 !important;
			width: 100%;
			pointer-events: all;
		}

		:global(.scrolly-text-container) {
			pointer-events: none;
			width: 100%;
			padding: 0 2rem;
		}
		:global(.step) {
			margin: 80vh auto;
			max-width: 600px;
			width: auto;
			height: auto;
			font-size: 1.25rem;
			padding: 0.5rem 1.5rem;
			background: var(--color-bg);
			border: 1px solid var(--color-dark-tan);
		}
		:global(.step p) {
			padding: 0;
		}
	}

	@media (max-width: 600px) {
		:global(.scrolly-text-container) {
			padding: 0 1rem;
		}
		:global(.step) {
			margin: 70vh auto;
		}
		:global(.step p) {
			font-size: var(--28px);
		}
		.text-blocks {
			max-width: 600px;
			margin-left: auto;
			margin-right: auto;
		}
	}

	@media (max-width: 425px) {
		.text-blocks {
			max-width: 90vw;
			margin-left: auto;
			margin-right: auto;
		}
		:global(.step) {
			padding: 0.5rem 1rem;
		}
	}
</style>
