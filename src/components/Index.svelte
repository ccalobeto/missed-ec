<script>
	import { getContext } from "svelte";
	import Missing from "$components/Missing.svelte";
	import Footer from "$components/Footer.svelte";

	const copy = getContext("copy");
</script>

<Missing {copy} />

<Footer />

<style>
	.text-blocks {
		max-width: 600px;
		margin-left: auto;
		margin-right: auto;
		margin-top: 15px;
		margin-bottom: 15px;
	}
</style>
