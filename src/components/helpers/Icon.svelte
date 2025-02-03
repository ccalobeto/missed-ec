<script>
	import feather from "feather-icons";
	export const directions = ["n", "ne", "e", "se", "s", "sw", "w", "nw"];

	let {
		name,
		direction = "n",
		width = "1.25em",
		height = "1.25em",
		stroke = undefined,
		strokeWidth = undefined
	} = $props();

	const icon = $derived(feather.icons[name]);
	const rotation = $derived(directions.indexOf(direction) * 45);

	$effect(() => {
		if (icon) {
			if (stroke) icon.attrs["stroke"] = stroke;
			if (strokeWidth) icon.attrs["stroke-width"] = strokeWidth;
		}
	});
</script>

{#if icon}
	<svg
		{...icon.attrs}
		style="width: {width}; height: {height}; transform: rotate({rotation}deg);"
	>
		<g>
			{@html icon.contents}
		</g>
	</svg>
{/if}

<style>
	svg {
		width: 1em;
		height: 1em;
		overflow: visible;
		transform-origin: 50% 50%;
	}
</style>
