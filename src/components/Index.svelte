<script>
	import { getContext } from "svelte";
	// import Footer from "$components/Footer.svelte";
	import Missed from "./Missed.svelte";

	const copy = getContext("copy");
</script>

<article>
	<Missed {copy} />
</article>

<!-- <Footer /> -->

<style>
	article {
		display: flex;
		flex-direction: column;
	}
</style>
