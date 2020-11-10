import functionsForUpdateDB
import pandas as pd
import  psycopg2
from dotenv import load_dotenv

import os

load_dotenv(verbose=True)



data = functionsForUpdateDB.database_add_lat_long()

data['Traffic is affected'] = pd.np.where(data['inc_detail_description'].str.contains('!!'), 'True', 'False')


no_db_data = functionsForUpdateDB.data_not_find_database()

print('Insert with succes')
print('Below site names does not find in database\n',no_db_data)

db_tt_list = functionsForUpdateDB.select_all_tt_number()

data['event_end_time'] = data['event_end_time'].map(str)
data['event_end_time'] = data['event_end_time'].map(lambda x: x if x != 'nan' else '9999-12-12' )
# dir_to_path_1 = '/home/gaus/Project/db_architecture/data/'
# site_list = pd.read_excel(dir_to_path_1+'SITELIST.xlsx','Incidents_ITSM', skiprows=3 )
#
try:
    connection = psycopg2.connect(user=os.getenv('USER_DB'),
                                  password=os.getenv('PASSWORD_DB'),
                                  host=os.getenv('HOST_DB'),
                                  port="5432",
                                  database=os.getenv('DB_NAME'))
    cursor_insert = connection.cursor()
    i = 0
    for index, row in data.iterrows():
        if not row['platform_inc_number'] in db_tt_list:
            print(row['platform_inc_number'])

            sql_query = f""" INSERT INTO api_app_itsmincidents ("platform_inc_number", "status_inc",
                    "priority_incident",
                    "inc_description",
                    "inc_detail_description",
                    "name_region",
                    "site_id",
                    "event_start_time",
                    "event_end_time",
                    "network_element",
                    "final_solution",
                    "long_site_id",
                    "lat_side_id",
                    "traffic_affected") VALUES
                    ('{row['platform_inc_number']}',
                    '{row['status_inc']}',
                    '{row['priority_incident']}',
                    %s,
                    %s,
                     '{row['name_region']}',
                    '{row['site_id']}',
               
                   
                    '{row['event_start_time']}',
                     '{row['event_end_time']}',
                    '{row['network_element']}',
                     '{row['final_solution']}',
                      '{row['LONG']}',
                     '{row['LAT']}',
                     '{row['Traffic is affected']}');"""

            cursor_insert.execute(sql_query,(row['inc_description'],row['inc_detail_description']))
            connection.commit()

        else:
            sql_update = f'''UPDATE api_app_itsmincidents
                            SET
                            "platform_inc_number" = '{row['platform_inc_number']}',
                            "status_inc" = '{row['status_inc']}',
                             "priority_incident"='{row['priority_incident']}',
                            "inc_description"= %s,
                            "inc_detail_description"=%s,
                            "name_region"= '{row['name_region']}',
                            "site_id"='{row['site_id']}',
                            "event_start_time"='{row['event_start_time']}',
                            "event_end_time"= '{row['event_end_time']}',
                            "network_element"='{row['network_element']}',
                            "final_solution"=  '{row['final_solution']}',
                            "long_site_id"= '{row['LONG']}',
                            "lat_side_id"='{row['LAT']}',
                            "traffic_affected"='{row['Traffic is affected']}'

                            WHERE "platform_inc_number" =  '{row['platform_inc_number']}'; '''

            cursor_insert.execute(sql_update,(row['inc_description'],row['inc_detail_description']))
            connection.commit()

except (Exception, psycopg2.Error) as error :
    print ("Error insert last\n", error)

finally:
    if(connection):
        cursor_insert.close()
        connection.close()
        print("PostgreSQL connection is closed")




#
# sql_query = '''SELECT "Incident Number - INC"  from incidents'''
# cursor_insert.execute(sql_query)
# rows_query_incidents = cursor_insert.fetchall()
# a_list = []
#
#
# for row in rows_query_incidents:
#     a_list.append(row[0])














# engine = create_engine('postgresql://gauss:010505de@localhost:5432/inc_test')
# print('Df to SQL inserting')
# data.to_sql('incidents', engine, if_exists='replace')






