import psycopg2

def connect(user: str, password: str, host: str, port: str, database: str) -> classmethod:
    connection = psycopg2.connect(user = user,\
                                password = password,\
                                host = host,\
                                port = port,\
                                database=database)
    return connection


def count_validation(connection: classmethod, year : str) -> classmethod:
    connection = connection
    cursor = connection.cursor()

    count_validation = f'select vs.station, count(num_ticket) from validation{year} val join vestibuls vs on val.id_vestib = vs.pl_id group by vs.station'
    cursor.execute(count_validation)
    stations = cursor.fetchall()

    connection.commit()

    return stations
