<script>
	import { getContext } from "svelte";
	// import Footer from "$components/Footer.svelte";
	import Missed from "./Missed.svelte";

	const copy = getContext("copy");
</script>

<section>
	<h1>{copy.title}</h1>
	<p>{@html copy.description}</p>
	<img src="missing-child.jpg" alt="" />
</section>

<article>
	<Missed {copy} />
</article>

<!-- <Footer /> -->

<style>
	article {
		display: flex;
		flex-direction: column;
	}
	section {
		border: 2px solid var(--color-gray-300);
		padding: 5px;
		margin: 5px;
		box-sizing: border-box;
	}
	section h1 {
		font-family: var(--serif);
		font-weight: 300;
		font-size: clamp(1.8rem, calc(7vw + 0.8rem), 3.5rem);
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
		aspect-ratio: 1.2;
		margin: auto;
	}
</style>
