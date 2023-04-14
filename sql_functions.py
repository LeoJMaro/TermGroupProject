from SECRETS import PASSWORD, USER, DATABASE
import mysql.connector


def executeQueryAndReturnResult(query, host='localhost', username=USER, password=PASSWORD, port=3306,
                                database=DATABASE):
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=DATABASE) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.column_names, cursor.fetchall()

def executeQueryAndReturnResultNoColumnName(query, host='localhost', username=USER, password=PASSWORD, port=3306,
                                            database=DATABASE):
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=DATABASE) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


def executeQueryAndCommit(query, host='localhost', username=USER, password=PASSWORD, port=3306, database=DATABASE):
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=database) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            return cursor.rowcount

