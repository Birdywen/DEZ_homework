import os
import pandas as pd
from sqlalchemy import create_engine
url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'
os.system(f'wget {url}')
engine = create_engine(f'postgresql://root:root@localhost:5432/ny_taxi')
engine.connect()
df_zones = pd.read_csv('taxi_zone_lookup.csv')
df_zones.to_sql(name='zones', con=engine, if_exists='replace')