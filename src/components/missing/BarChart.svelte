<script>
	import { LayerCake, Svg } from "layercake";
	import { scaleBand } from "d3-scale";

	import AxisY from "$components/missing/_components/AxisY.svelte";
	import AxisX from "$components/missing/_components/AxisX.svelte";
	import Bar from "$components/missing/_components/Bar.svelte";

	import { categories } from "$data/preparedData.js";

	export let item;
	const xKeyCat = "percentage";
	const yKeyCat = "cardinality";

	console.log("items=>", item);
	console.log("data=>", categories);
</script>

<h1>This is a bar Chart</h1>
<div class="bar-container">
	<LayerCake
		padding={{ bottom: 20, left: 100 }}
		x={xKeyCat}
		y={yKeyCat}
		yScale={scaleBand().paddingInner(0.05)}
		xDomain={[0, null]}
		data={categories}
	>
		<Svg>
			<AxisX tickMarks baseline snapLabels />
			<AxisY tickMarks gridlines={false} />
			<Bar />
		</Svg>
	</LayerCake>
</div>

<style>
	.bar-container {
		width: 80%;
		height: 250px;
		margin: 25px auto;
	}
</style>
