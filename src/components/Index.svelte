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
	<p class="byline">{@html copy.byline}</p>
</section>

<article>
	<Missed {copy} />
</article>

<!-- <Footer /> -->
<div class="footer">
	<p class="made-with">{@html copy.footer}</p>
</div>

<style>
	article {
		display: flex;
		flex-direction: column;
	}
	section {
		/* border: 2px solid var(--color-gray-300); */
		padding: 5px;
		margin: 5px;
		box-sizing: border-box;
		/* justify-items: center; */
	}
	section h1 {
		font-family: var(--serif);
		font-weight: 300;
		font-size: clamp(1.8rem, calc(7vw + 0.8rem), 3.5rem);
		text-align: center;
	}

	section p {
		font-size: clamp(1rem, 2vw + 0.5rem, 2rem);
		font-style: italic;
		text-align: center;
		max-width: clamp(300px, 80vw, 1200px);
		margin-left: auto;
		margin-right: auto;
	}

	section img {
		aspect-ratio: 1.2;
		margin: auto;
	}

	.byline {
		font-family: var(--mono, --font-body);
		font-size: var(--16px);
		font-style: normal;
	}

	.footer {
		padding: 5px;
		margin: 5px;
		box-sizing: border-box;
		text-align: center;
	}

	.made-with {
		font-family: var(--mono, --font-body);
		font-style: normal;
		font-size: clamp(0.5rem, 1.2vw + 0.5rem, 1.8rem);
		margin: 30px;
	}
</style>
