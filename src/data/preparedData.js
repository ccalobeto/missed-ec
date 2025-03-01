import data from '$data/summaries.json';
import topoFile from '$data/support/ecuador-tm-50k.json';
import copy from "$data/copy.json";

const kpisForCharts = {
  'bar': ['historical-cases', 'historical-cases-missed', 'age_range', 'category'],
  'donut': ['sex'],
  'choropleth': ['nominal-cases', 'relative-cases']
}

export const dataLookupForCharts = (keyChart) => {

  let preparedDataForCharts = [];
  const dataLookup = new Map();
  const isMap = keyChart === 'choropleth';
  const filteredData = data.filter(d => {
    return kpisForCharts[keyChart].includes(d.kpi)
  })
  preparedDataForCharts = filteredData.map(d => {
    return {
      kpi: d.kpi,
      data: d.data.map(d => {
        return (!isMap) ? {
          cardinality: d.cardinality,
          value: Number.isInteger(d.count) ? d.count : d.count.toFixed(1),
          percentage: isMap ? null : Number.parseFloat(d.percentage.toFixed(1)),
        }
          : {
            id: d.id,
            value: Number.isInteger(d.count) ? d.count : d.count.toFixed(1),
          }
      })
    }
  })

  let idDataList = [];
  if (isMap) {
    preparedDataForCharts.forEach(dataset => {
      idDataList = dataset.data.map(d => d.id);
      dataset.data.push(...populateData(idDataList))
    })
  }

  preparedDataForCharts.forEach(d => {
    dataLookup.set(d.kpi, d.data);
  });
  return dataLookup

}

function populateData(idDataList) {
  const cartography = topoFile.objects['level3']
  const cantonsList = cartography.geometries.map(d => d.properties.id);
  const cantonsDataNotFound = cantonsList.filter(x => !idDataList.includes(x));
  let zeroData = []

  cantonsDataNotFound.forEach(element => {
    zeroData.push({
      id: element,
      value: 0,
    })
  });
  return zeroData

}

export const indexOfCopyToKpiAssociation = (copyBodyType, keyChart) => {

  let indexToKpi = {};
  const indexOfCopy = copy.body.filter((d, i) => {
    if (d.type === copyBodyType) {
      d.index = i;
      return true;
    }
    return false;
  });

  const kpis = kpisForCharts[keyChart];

  if (indexOfCopy.length == kpis.length) {

    indexToKpi = indexOfCopy.map((d, i) => {
      return {
        [d.index]: kpis[i]
      };
    });
    return indexToKpi.reduce((a, b) => ({ ...a, ...b }), {});
  }
  else {
    console.log("Number of kpis in kpisForCharts must match with 'type' in body of copy.json");
  }

}

export const twoLevelflatten = (body) => {
  // flattens copy.body
  return body.flatMap((obj, i) => {
    if (obj.value.steps)
      return obj.value.steps.flatMap((step) => ({
        type: obj.type,
        index: i,
        step: step
      }));
    else
      return {
        type: obj.type,
        index: i,
        step: obj.value
      };
  })
}