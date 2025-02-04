import data from '$data/summaries.json';
import topoFile from '$data/ecuador-tm-50k.json';

const DISSAPEARENCE_YEAR = 2023;
const filteredData = data[5].data.filter(d => {
  return 'disappearance_year' in d && d.disappearance_year === DISSAPEARENCE_YEAR;
});

export const categories = data[3].data.map(d => {
  if ('cardinality' in d) {
    return {
      cardinality: d.cardinality,
      percentage: d.percentage
    };
  } else {
    return null;
  }
});

function populateData(data) {
  const cartography = topoFile.objects['level3']
  const cantonsList = cartography.geometries.map(d => d.properties.name);
  const cantonsDataList = filteredData.map(d => d.name);
  const cantonsDataNotFound = cantonsList.filter(x => !cantonsDataList.includes(x));
  let zerodata = []

  cantonsDataNotFound.forEach(element => {
    zerodata.push({
      name: element,
      myValue: 0,
    })
  });
  const concatData = [...data, ...zerodata];
  return concatData

}
export const stateData = () => {

  const mapData = filteredData.map(d => {
    if ('id' in d) {
      return {
        name: d.name,
        myValue: d.missedPer10k.toFixed(1),
      };
    }
  });

  return populateData(mapData)
}
console.log(stateData().length);