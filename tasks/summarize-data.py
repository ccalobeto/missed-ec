# This script generates a json file with all data summaries related to the svelte project
import pandas as pd
import json
import numpy as np

# set year of analysis
OBSERVED_YEAR = 2024 
# set the ratio of data to population
RATIO_COUNT = 10000

# output json file
OUTPUT_PATH = "./src/data/"
OUTPUT_JSON = 'summaries.json'
 
# The path is different in python in comparison with JS: it is the project path
FILE = "./src/data/output/long_data_with_cantonId.csv"
FILE2 = "./src/data/support/proyeccion_cantonal_total_2010-2020.csv"
FILE3 = "./src/data/support/categories.csv"

df = pd.read_csv(FILE, dtype={'id': 'str'})
df2 = pd.read_csv(FILE2, dtype={'Codigo': 'str'})
df3 = pd.read_csv(FILE3)

## fill data for missing years and unpivot projection population
maxYearData = df['disappearance_year'].max()
years = df2.filter(like='20').columns.to_list()
years = [int(x) for x in years]
maxYearProjection = max(years)
missingYears = list(range(maxYearProjection + 1, maxYearData + 1))
df2.columns = [x.lower() for x in df2.columns]
df2.rename(columns=lambda x: 'P' + x if x.startswith('20') else x, inplace=True)
df2.rename(columns={'codigo': 'cantonId', 'nombre de canton': 'cantonName'}, inplace=True)
for i in missingYears:
  df2['P' + str(i)] = df2['P' + str(maxYearProjection)]
df2 = pd.wide_to_long(df2, stubnames='P', i=['cantonId', 'cantonName'], j='year').reset_index()
df2.rename(columns={'P': 'proj_population'}, inplace=True)

# join
all_data_ = pd.merge(df, df3, on='motivo_desaparicion_obs', how='left')

# complete missing data
all_data_['category'].replace(np.nan, 'DESAPARECIDO', inplace=True)
all_data_['tipology'].replace(np.nan, 'DESAPARECIDO', inplace=True)

# historical
agg_by_year = all_data_.groupby(['country', 'disappearance_year']).size().reset_index(name='count')
agg_by_year['percentage'] = 100 * (agg_by_year['count'] / agg_by_year['count'].sum())
agg_by_year['disappearance_year'] = agg_by_year['disappearance_year'].astype(str)
agg_by_year.rename(columns={'disappearance_year': 'cardinality'}, inplace=True)

agg_by_year_missed = all_data_[all_data_['days_gone'].isnull()].groupby(['country', 'disappearance_year']).size().reset_index(name='count')
agg_by_year_missed['percentage'] = 100 * (agg_by_year_missed['count'] / agg_by_year_missed['count'].sum())
agg_by_year_missed['disappearance_year'] = agg_by_year_missed['disappearance_year'].astype(str)
agg_by_year_missed.rename(columns={'disappearance_year': 'cardinality'}, inplace=True)

# filter by observed year
# all_data_.to_csv('./src/data/all_data.csv', index=False)
all_data = all_data_[all_data_['disappearance_year'] == OBSERVED_YEAR]

# aggregations
agg_by_age_range = all_data.groupby(['country', 'rango_edad']).size().reset_index(name='count')
agg_by_age_range['percentage'] = 100 * (agg_by_age_range['count'] / agg_by_age_range['count'].sum())
agg_by_age_range.rename(columns={'rango_edad': 'cardinality'}, inplace=True)

agg_by_tipology = all_data.groupby(['country', 'tipology']).size().reset_index(name='count')
agg_by_tipology['percentage'] = 100 * (agg_by_tipology['count'] / agg_by_tipology['count'].sum())
agg_by_tipology.rename(columns={'tipology': 'cardinality'}, inplace=True)

agg_by_category = all_data.groupby(['country', 'category']).size().reset_index(name='count')
agg_by_category['percentage'] = 100 * (agg_by_category['count'] / agg_by_category['count'].sum())
agg_by_category.rename(columns={'category': 'cardinality'}, inplace=True)

agg_by_sex = all_data.groupby(['country', 'sexo']).size().reset_index(name='count')
agg_by_sex['percentage'] = 100 * (agg_by_sex['count'] / agg_by_sex['count'].sum())
agg_by_sex.rename(columns={'sexo': 'cardinality'}, inplace=True)

agg_by_canton = all_data.groupby(['country', 'disappearance_year','id', 'name']).size().reset_index(name='count')
agg_by_canton = agg_by_canton.merge(df2, how='left', left_on=['id', 'disappearance_year'],right_on=['cantonId', 'year'])
agg_by_canton['missedPer10k'] = agg_by_canton['count'] / agg_by_canton['proj_population'] * RATIO_COUNT

nominal_cases = agg_by_canton[['country', 'id', 'name', 'count']]
relative_cases = agg_by_canton[['country', 'id', 'name', 'missedPer10k']]
relative_cases.rename(columns={'missedPer10k': 'count'}, inplace=True)

# print(agg_by_sex)
# print(agg_by_sex.dtypes)

# convert multidataframes to json
map_summaries = {'historical-cases': agg_by_year, 
                 'historical-cases-missed': agg_by_year_missed,
                 'age_range': agg_by_age_range, 
                 'tipology': agg_by_tipology, 
                 'category': agg_by_category, 
                 'sex': agg_by_sex,
                 'nominal-cases': nominal_cases,
                 'relative-cases': relative_cases
                 }
summaries = []
for k,v in map_summaries.items():
  row_summary = {}
  column = v.columns.to_list()[1]
  row_summary['kpi'] = k
  if k != 'historical-cases' and k != 'historical-cases-missed':
    row_summary['observed_year'] = OBSERVED_YEAR
  if k != 'relative-cases':
    row_summary['total_rows'] = int(v['count'].sum())
  # this is the key. to_json method return str so you have to reconvert to a list with json.loads. finally when you dump it doesn't display with "\"
  row_summary['data'] = json.loads(v.to_json(orient='records'))
  summaries.append(row_summary)

with open(OUTPUT_PATH + OUTPUT_JSON, 'w') as f:
  json.dump(summaries, f)

stats = {
  'total_input_rows': df.shape[0],
  'total_join_data_rows': all_data_.shape[0],
}

print('stats:', stats)
print('JSON file created.')