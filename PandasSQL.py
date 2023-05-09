import psycopg2
from psycopg2 import Error
import pyodbc
import pandas as pd
# Подключение к существующей базе данных
connection = psycopg2.connect(user = "shad112_prmetro",\
                                password = "1234",\
                                host = "91.190.239.132",\
                                port = "5432",\
                                database="SHAD112_Pr_Metro")


def connect(connection):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**connection)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        #sys.exit(1)
    print("Connection successful")
    return conn


def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()

    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df

conn = connect(connection)
column_names = ["id", "source"]
# Execute the "SELECT *" query
df = postgresql_to_dataframe(conn, "select * from goods", column_names)
df.head(2)

# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("Соединение с PostgreSQL закрыто")






# sq = pd.read_sql_query("SELECT * FROM goods", connection)
# df = pd.DataFrame(sq.head(2))
# print(df)
