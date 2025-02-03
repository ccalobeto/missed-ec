<script>
	import ChoroplethMap from "$components/Missing/ChoroplethMap.svelte";
	import BarChart from "$components/Missing/BarChart.svelte";
	import DonutChart from "$components/Missing/DonutChart.svelte";

	export let copy;
</script>

<div class="article">
	{#each Object.keys(copy) as block, idx}
		<div class="block-{block}">
			{#each copy[block] as item, index}
				<div class="section-{item['section']}">
					{#each copy[block][index]["content"] as item, i}
						<div class="type-{item['type']}">
							{#if item.type === "text"}
								<p class="text-blocks">{@html item.value}</p>
							{/if}
							{#if item.type === "donut-chart"}
								<DonutChart {item} />
							{/if}
							{#if item.type === "bar-chart"}
								<BarChart {item} />
							{/if}
							{#if item.type === "choropleth-map"}
								<ChoroplethMap {item} />
							{/if}
						</div>
					{/each}
				</div>
			{/each}
		</div>
	{/each}
</div>

<style>
	.text-blocks {
		max-width: 600px;
		margin-left: auto;
		margin-right: auto;
	}
	.article > * {
		color: #eee;
	}
</style>
