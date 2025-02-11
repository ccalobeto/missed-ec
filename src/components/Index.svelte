<script>
	import { getContext } from "svelte";
	import Footer from "$components/Footer.svelte";
	import ScrollyTelling from "./ScrollyTelling.svelte";

	const copy = getContext("copy");
</script>

<h2 class="title">{copy.title}</h2>
<p class="text-blocks">{@html copy.description}</p>

<ScrollyTelling {copy} />

<!-- <Footer /> -->

<style>
	.title {
		max-width: 14em;
		margin: 0 auto;
		padding: 32px 0;
	}
	.text-blocks {
		max-width: 600px;
		margin-left: auto;
		margin-right: auto;
		margin-top: 15px;
		margin-bottom: 15px;
	}
</style>
