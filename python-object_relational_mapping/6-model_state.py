#!/usr/bin/python3
"""Start link class to table in database"""

# Required to read CLI input arguments
import sys
# Required to create a driver to interact with databases.
from sqlalchemy import (create_engine)
# Required to get tools to examine a database structure.
from sqlalchemy import inspect
# Required to create the database tables using our Python class models.
from model_state import Base, State


if __name__ == "__main__":
    # Improving the code provided by setting
    #   fallback values.
    db_user = sys.argv[1] if len(sys.argv) > 1 else 'root'
    db_passwd = sys.argv[2] if len(sys.argv) > 2 else 'root'
    db_name = sys.argv[3] if len(sys.argv) > 3 else 'hbtn_0e_6_usa'
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        # .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        .format(db_user, db_passwd, db_name),
        # echo=True,  # Activates "verbose mode" for engine
        pool_pre_ping=True
    )
    # Order to create any table which doesn't exist yet for a class
    Base.metadata.create_all(engine)

    # Basic addition to provided code: simple declaration of
    #   "what should exist" from the Classes declared.
    print("Tables models:", Base.metadata.tables.keys())
    # More in-depth verification of what was done
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print(f"Tables existing in :{db_name}", tables)
