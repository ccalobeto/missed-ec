<script>
	import { getContext } from "svelte";
	// import Footer from "$components/Footer.svelte";
	import Missed from "./Missed.svelte";

	const copy = getContext("copy");
</script>

<Missed {copy} />

<!-- <Footer /> -->

<style>
	.text-blocks {
		max-width: 600px;
		margin-left: auto;
		margin-right: auto;
		margin-top: 15px;
		margin-bottom: 15px;
	}
</style>
