import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv(verbose=True)
def database_add_lat_long():
    try:
        connection = psycopg2.connect(user=os.getenv('USER_DB'),
                                      password=os.getenv('PASSWORD_DB'),
                                      host=os.getenv('HOST_DB'),
                                      port = "5432",
                                      database=os.getenv('DB_NAME'))
        cursor = connection.cursor()
        print('Succes connect')
        dir_to_path = os.getenv('DIR_TO_PATH')
        data_set = pd.read_excel(dir_to_path+'incidents.xlsx')

        print('Succes import data')

        list_of_query = []
        for index , row in data_set.iterrows():
            site_name = row['site_id']
            query_SQL = f'''SELECT "site_name", "long_id", "lat_id" FROM api_app_coordinates WHERE "site_name" LIKE '%{site_name}%' LIMIT 1;'''

            cursor.execute(query_SQL)
            rows_query = cursor.fetchall()

            for row_query in rows_query:
                name_query = row_query[0]
                long_query = row_query[2]
                lat_query = row_query[1]
                s_list = list((
                    row['platform_inc_number'],
                    row['status_inc '],
                    row['priority_incident'],
                    row[' inc_description'],
                    row[' inc_detail_description '],
                    row['name_region'],
                    row['site_id'],
                    row[' event_start_time'],
                    row[' event_end_time '],
                    row[' network_element'],
                    row['final_solution '],
                    lat_query,
                    long_query))
                list_of_query.append(s_list)

        print('SQL Succes executed query')
        print('Creatind a dataframe \n')

        data_result = pd.DataFrame(list_of_query, columns=['platform_inc_number',
                                   'status_inc',
                                   'priority_incident',
                                   'inc_description',
                                'inc_detail_description',
                                   'name_region',
                                    'site_id',
                                'event_start_time',
                                   'event_end_time',
                                   'network_element',
                                   'final_solution',
                                     'LONG' ,
                                     'LAT'])


        return data_result



    except (Exception, psycopg2.Error) as error :
        print ("Error ocu", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



def data_not_find_database():


    list_with_false = []

    for index, row in data_set.iterrows():
        if row['site_id'] not in df_with_coordinates['site_id'].values:
            list_with_false.append(row['site_id'])


    duplicate_filtered = list(dict.fromkeys(list_with_false))


    return duplicate_filtered


def select_all_tt_number():
    try:
        connection = psycopg2.connect(user=os.getenv('USER_DB'),
                                      password=os.getenv('PASSWORD_DB'),
                                      host=os.getenv('HOST_DB'),
                                      port="5432",
                                      database=os.getenv('DB_NAME'))

        cursor_insert = connection.cursor()

        sql_query = '''SELECT "platform_inc_number"  from api_app_itsmincidents'''
        cursor_insert.execute(sql_query)
        rows_query_incidents = cursor_insert.fetchall()
        a_list = []
        for row in rows_query_incidents:
            a_list.append(row[0])



        return a_list



    except (Exception, psycopg2.Error) as error :
        print ("Error insert\n", error)

    finally:
        #closing database connection.
        if(connection):
            cursor_insert.close()
            connection.close()
            print("PostgreSQL connection is closed")




df_with_coordinates = database_add_lat_long()

dir_to_path = os.getenv('DIR_TO_PATH')
data_set = pd.read_excel(dir_to_path+'incidents.xlsx')

#print(df_with_coordinates)
# data_not_find_database()
