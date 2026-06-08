#!/usr/bin/python3
"""Lists states matching provided 'name pattern' in a safe way"""


import sys      # Required to read standard input arguments (sys.argv)
import MySQLdb  # Required to interact with MySQL server


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("""
            Please db connection infos in that order: mySql user name,
            related password, name of the database to manipulate.
            Plus the 'name' pattern you want to search among all states.
            The script will expect that MySQL in installed on the same machine
              (aka "localhost") and uses default port (= 3306).
            """)

    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_database = sys.argv[3]
    db_host = "localhost"
    db_port = 3306  # MUST be an actual integer

    mysql_connection = MySQLdb.connect(
        host=db_host,
        user=db_user,
        passwd=db_passwd,
        port=db_port,
        db=db_database
    )

    cursor = mysql_connection.cursor()
    # states_table = "states"  "Dynamic table name" CANNOT WORK with .execute
    searched_state = sys.argv[4]

    # Confer https://peps.python.org/pep-0249/#id20
    #   for details on "prepared requests" with the driver
    #   sanitizing the string itself.
    search_specific_state_query = """
        SELECT * FROM states
        WHERE name = BINARY %s
        ORDER BY id
    """
    cursor.execute(
        search_specific_state_query,
        (searched_state,)  # TUPLE so , even if only one element inside.
    )

    matching_state_found = cursor.fetchall()
    for state in matching_state_found:
        print(state)

    cursor.close()
    mysql_connection.close()
