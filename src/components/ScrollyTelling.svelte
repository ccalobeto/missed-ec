<script>
	import Scrolly from "./helpers/Scrolly.svelte";
	import Charts from "./missing/Charts.svelte";

	export let copy;
	let value;

	const scrollyTeller = copy.body.filter((d) => d.section === "charts")[0]
		.content;
	const steps = scrollyTeller.map((d) => d.value.steps).flat();

	console.log("ScrollyTelling: storyTeller => ", scrollyTeller);
</script>

<section>
	<div class="section-container">
		<div class="sticky">
			<Charts step={value} {scrollyTeller} />
		</div>
		<div class="steps-container">
			<!-- {console.log("ScrollyTelling: scrollyValue => ", value)} -->
			<Scrolly bind:value>
				{#each steps as step, i}
					<div class="step" class:active={value === i}>
						<div class="step-content">{@html step.value}</div>
					</div>
				{/each}
				<div class="spacer"></div>
			</Scrolly>
		</div>
	</div>
</section>

<style>
	.spacer {
		height: 40vh;
	}

	.sticky {
		position: sticky;
		top: 10%;
		flex: 1 1 60%;
		width: 60%;
	}

	.section-container {
		margin-top: 1em;
		text-align: center;
		transition: background 100ms;
		display: flex;
	}

	.step {
		height: 80vh;
		display: flex;
		place-items: center;
		justify-content: center;
	}

	.step-content {
		font-size: 1rem;
		background: whitesmoke;
		color: #ccc;
		border-radius: 5px;
		padding: 0.5rem 1rem;
		display: flex;
		flex-direction: column;
		justify-content: center;
		transition: background 500ms ease;
		box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2);
		text-align: left;
		width: 75%;
		margin: auto;
		max-width: 500px;
	}

	.step.active .step-content {
		background: green;
		color: black;
	}

	.steps-container,
	.sticky {
		height: 100%;
	}

	.steps-container {
		flex: 1 1 40%;
		z-index: 10;
	}

	/* Comment out the following line to always make it 'text-on-top' */
	@media screen and (max-width: 768px) {
		.section-container {
			flex-direction: column-reverse;
		}
		.sticky {
			width: 95%;
			margin: auto;
		}
	}
</style>
