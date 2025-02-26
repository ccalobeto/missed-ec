# This script generates a csv cleaned file with accumulated data.
import pandas as pd
import numpy as np
import unidecode
import json
import topojson as tp
import geopandas as gpd
from shapely.geometry import Point, box


# The path is different in python in comparison with JS: it is the project path
FILE = "./src/data/input/mdi_personas_desaparecidas_2017_2024.csv"
FILE1 = "./src/data/input/mdi_personas_desaparecidas_2025_enero.csv"
topo_file = "./src/data/support/ecuador-tm-50k.json"

OUTPUT_LONG_DATA = "./src/data/output/long_data.csv"
'./src/lib/data/output/long_data.csv'
OUTPUT_LONG_DATA_WITH_CANTONID = "./src/data/output/long_data_with_cantonId.csv"

df = pd.read_csv(FILE)
df1 = pd.read_csv(FILE1)

# rename columns
newColumns = {
  'edad_aprox.': 'edad',
  'motivo_desaparcion': 'motivo_desaparicion',
  'motivo_desaparcion_obs.': 'motivo_desaparicion_obs',
}
newColumns1 = {
  'latitud_desaparicion': 'latitud',
  'longitud_desaparicion': 'longitud',
  'edad_aprox.': 'edad',
  'motivo_desaparcion': 'motivo_desaparicion',
  'motivo_desaparcion_obs.': 'motivo_desaparicion_obs',
}
df.rename(columns=newColumns, inplace=True)
df1.rename(columns=newColumns1, inplace=True)

# concatenate df and df1
df2 = pd.concat([df, df1], ignore_index=True)
# reorder columns for df12
df2 = df2[['provincia', 'latitud', 'longitud', 'edad', 'sexo', 'motivo_desaparicion', 'motivo_desaparicion_obs', 'fecha_desaparicion', 'estado_desaparecido', 'fecha_localizacion', 'latitud_localizacion', 'longitud_localizacion']]

# reemplace SIN_DATO with NaN
df2.replace('INVESTIGACION', np.nan, inplace=True)

# remove last space
df2['estado_desaparecido'] = df2['estado_desaparecido'].str.strip()
df2['motivo_desaparicion_obs'] = df2['motivo_desaparicion_obs'].str.strip()

# do some cleaning and transform. Only float accept nan values
df2['motivo_desaparicion_obs'] = df2['motivo_desaparicion_obs'].str.upper()
df2['latitud_localizacion'] = df2['latitud_localizacion'].astype('float32')
df2['longitud_localizacion'] = df2['longitud_localizacion'].astype('float32')

# fill missing values of edadwith the mean
meanAgeOfYoungAdults = df2['edad'].mean()
df2.loc[df2['edad'].isna(), 'edad'] = meanAgeOfYoungAdults

## add categories to df
bins = [-1, 12, 17, 24, 35, 50, 64, np.inf]
labels = ['De 0 - 12', 'De 13 - 17', 'De 18 - 24', 'De 25 - 35', 'De 36 - 50', 'De 51 - 65', 'De 65 a más']
df2['rango_edad'] = pd.cut(df2['edad'], bins, labels=labels)

# transform to string date to date
df2['fecha_desaparicion'] = pd.to_datetime(df2['fecha_desaparicion'], format='%d/%m/%Y')
df2['fecha_localizacion'] = pd.to_datetime(df2['fecha_localizacion'], format='%d/%m/%Y')

# add extra columns for analysis
df2['disappearance_year'] = df2['fecha_desaparicion'].dt.year
df2['disappearance_month'] = df2['fecha_desaparicion'].dt.month
df2['disappearance_day'] = df2['fecha_desaparicion'].dt.day
df2['days_gone'] = (df2['fecha_localizacion'] - df2['fecha_desaparicion']).dt.days
# add country ISO 3166-1 A-3 code
df2['country'] = 'ECU'
df2['row_id'] = df2.index

# remove accents
cols_accents_to_remove = ['motivo_desaparicion', 'motivo_desaparicion_obs', 'rango_edad']
for column in cols_accents_to_remove:
  df2[column] = df2[column].apply(lambda x: unidecode.unidecode(x) if x is not np.nan else x)

## detect the cantonId from coordinates
# load cartography canton and convert to geopandas
with open(topo_file) as f:
  carto_load = json.load(f)
canton_topo = tp.Topology(carto_load, object_name='level3')
canton_dict = json.loads(canton_topo.to_geojson())
canton_gdf = gpd.GeoDataFrame.from_features(canton_dict['features'])

# convert bbox into a polygon
geom = box(*canton_gdf.total_bounds)

# prepare the coordinates and convert to geopandas
df2['coordinates'] = list(zip(df2['longitud'], df2['latitud']))
df2['coordinates'] = df2['coordinates'].apply(Point)
# check if the coordinates are inside Ecuador
df2['in_bounds'] = df2.apply(lambda x: geom.contains(x['coordinates']), axis=1)
df2_gdf = gpd.GeoDataFrame(df2, geometry='coordinates')

# https://autogis-site.readthedocs.io/en/2019/notebooks/L3/spatial_index.html
# spatial join
sjoin = gpd.sjoin(df2_gdf, canton_gdf, how='left')
df3 = pd.DataFrame(sjoin)

# imputation
df3['observation'] = 'no'
df3.loc[(df3['id'].isna() & df3['in_bounds']), 'observation'] = 'imputed with closer cantonId'
df3['index'] = df3.index
df3.sort_values(['provincia', 'latitud', 'longitud', 'name'], ascending=[True, True, True, True], inplace=True, ignore_index=True)
df3[['id', 'name']] = df3[['id', 'name']].fillna(method='ffill')
# not impute the rows out of bounds
df3.loc[~df3['in_bounds'],['id', 'name']] = np.nan
df3.sort_values('index', inplace=True)

# remove unused columns
df3.drop(columns=['coordinates','index_right', 'index'], inplace=True)

# save files
df2.to_csv(OUTPUT_LONG_DATA, index=False)
df3.to_csv(OUTPUT_LONG_DATA_WITH_CANTONID, index=False)

stats = {
  'total_input_rows': df.shape[0] + df1.shape[0],
  'total_long_data_rows': df2.shape[0],
  'total_long_data_with_cantonId_rows': df3.shape[0],
  # 'total_rows_without_cantonId': df2[df2['id'].isna()].shape[0],
}

print('stats:', stats)
print('2 CSV files created')