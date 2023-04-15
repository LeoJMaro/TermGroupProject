from SECRETS import PASSWORD, USER, DATABASE
import mysql.connector


def executeQueryAndReturnResult(query, host='localhost', username=USER, password=PASSWORD, port=3306,
                                database=DATABASE):
    """
    Executes a MySQL query and returns the result
    :param query: (str) The SQL query to execute
    :param host: (str) The host where the database is located (default is 'localhost')
    :param username: (str) The username to use for the database connection (default is the value imported from SECRETS)
    :param password: (str) The password to use for the database connection (default is the value imported from SECRETS)
    :param port: (int) The port to use for the database connection (default is 3306)
    :param database: (str) The name of the database to use (default is the value imported from SECRETS)
    :return: (tuple) A tuple containing the column names and fetched rows as tuples
    """
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=DATABASE) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.column_names, cursor.fetchall()


def executeQueryAndReturnResultNoColumnName(query, host='localhost', username=USER, password=PASSWORD, port=3306,
                                            database=DATABASE):
    """
    Executes a MySQL query and returns the result without column names
    :param query: (str) The SQL query to execute
    :param host: (str) The host where the database is located (default is 'localhost')
    :param username: (str) The username to use for the database connection (default is the value imported from SECRETS)
    :param password: (str) The password to use for the database connection (default is the value imported from SECRETS)
    :param port: (int) The port to use for the database connection (default is 3306)
    :param database: (str) The name of the database to use (default is the value imported from SECRETS)
    :return: (list) A list of fetched rows as tuples
    """
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=DATABASE) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


def executeQueryAndCommit(query, host='localhost', username=USER, password=PASSWORD, port=3306, database=DATABASE):
    """
    Executes a MySQL query and commits the changes
    :param query: (str) The SQL query to execute
    :param host: (str) The host where the database is located (default is 'localhost')
    :param username: (str) The username to use for the database connection (default is the value imported from SECRETS)
    :param password: (str) The password to use for the database connection (default is the value imported from SECRETS)
    :param port: (int) The port to use for the database connection (default is 3306)
    :param database: (str) The name of the database to use (default is the value imported from SECRETS)
    :return: (int) Count of affected rows
    """
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=database) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            return cursor.rowcount
