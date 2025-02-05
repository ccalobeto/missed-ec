import data from '$data/summaries.json';
import topoFile from '$data/support/ecuador-tm-50k.json';

const DISSAPEARENCE_YEAR = 2023;
const filteredData = data[5].data.filter(d => {
  return 'disappearance_year' in d && d.disappearance_year === DISSAPEARENCE_YEAR;
});

const kpisForCharts = {
  'bar': ['category', 'age_range'],
  'donut': ['tipology', 'sex']
}

export const dataLookupForCharts = (keyChart) => {

  const dataLookup = new Map()
  const filteredBarData = data.filter(d => {
    return kpisForCharts[keyChart].includes(d.kpi);
  }).map(d => {
    return {
      kpi: d.kpi,
      data: d.data.map(d => {
        return {
          cardinality: d.cardinality,
          percentage: Number.parseFloat(d.percentage.toFixed(1)),
        };
      })
    }
  })

  filteredBarData.forEach(d => {
    dataLookup.set(d.kpi, d.data);
  });
  return dataLookup

}

export const categories = data[3].data.map(d => {
  if ('cardinality' in d) {
    return {
      cardinality: d.cardinality,
      percentage: Number.parseFloat(d.percentage.toFixed(1)),
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
console.log(`data from ${stateData().length} cantons`);