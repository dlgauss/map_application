import os
from dotenv import load_dotenv

import psycopg2
import pandas as pd


load_dotenv(verbose=True)

df = pd.read_excel(f'/home/gauss/Projects/map-app/back-end/data/bd_data.xlsx')


conn = psycopg2.connect(host=os.getenv('HOST_DB'),
                        port=5432,
                        user=os.getenv('USER_DB'),
                        password=os.getenv('PASSWORD_DB'),
                        database=os.getenv('DB_NAME'))

print('Connected')
for index, row in df.iterrows():

    query = f"""INSERT INTO api_app_coordinates("site_name","address","long_id", "lat_id", "region", "town") VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (row['site_name'], row['address'],row["long"],row["lat"], row['region'], row['town'])
    cursor = conn.cursor()
    cursor.execute(query, record_to_insert)

    conn.commit()


conn.close()

print('Connect closed')


