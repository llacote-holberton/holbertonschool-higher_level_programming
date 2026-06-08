#!/usr/bin/python3
"""Lists cities and their state ordered by city id"""


import sys      # Required to read standard input arguments (sys.argv)
import MySQLdb  # Required to interact with MySQL server


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("""
            Please db connection infos in that order: mySql user name,
            related password, name of the database to manipulate.
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

    # Confer https://peps.python.org/pep-0249/#id20
    #   for details on "prepared requests" with the driver
    #   sanitizing the string itself.
    list_cities_query = """
        SELECT c.id, c.name, s.name
        FROM cities as c
        JOIN states as s
          ON c.state_id = s.id
        ORDER BY c.id;
    """
    cursor.execute(list_cities_query)

    all_cities_list = cursor.fetchall()
    for city in all_cities_list:
        print(city)

    cursor.close()
    mysql_connection.close()
