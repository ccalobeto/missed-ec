<script>
	import "$styles/app.css";
	import Header from "$components/Header.svelte";

	export let children;
</script>

<!-- <Header /> -->
<main id="content">
	{@render children?.()}
</main>
