#!/usr/bin/python3
"""Reads a table from MySQL database"""


import sys      # Required to read standard input arguments (sys.argv)
import MySQLdb  # Required to interact with MySQL server


if __name__ == "__main__":
    # Ensure user provides all required infos
    if len(sys.argv) != 4:
        print("""
            Please db connection infos in that order: mySql user name,
            related password, name of the database to manipulate.
            The script will expect that MySQL in installed on the same machine
              (aka "localhost") and uses default port (= 3306).
            """)

    # print(sys.argv) NOTE: first argument is the script name as in C.
    db_user = sys.argv[1]
    db_pwd = sys.argv[2]
    db_host = "localhost"
    db_port = "3306"
    db_name = sys.argv[3]

    db_connection = MySQLdb.connect(
        host=db_host,
        user=db_user,
        passwd=db_pwd,
        db=db_name
    )

    cursor = db_connection.cursor()

    # We predefine the query for readability.
    list_states_query = "SELECT * FROM states ORDER BY id"
    # Execution just "places a cursor just at the start of result set"
    # states_list = cursor.execute(list_states_query)
    cursor.execute(list_states_query)
    # BUT we need to actually retrieve some or all with "fetchxxx".
    states_list = cursor.fetchall()
    for state in states_list:
        print(state)
