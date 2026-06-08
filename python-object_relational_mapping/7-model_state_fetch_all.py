#!/usr/bin/python3
"""Reads info from States table using Alchemy ORM as interface"""

# Required to read CLI input arguments
import sys
# Required to create a driver to interact with databases.
from sqlalchemy import (create_engine)
# Required to get tools to examine a database structure.
from sqlalchemy import inspect
# Required to exploit the db tables using our Python class models.
from model_state import Base, State
# Required to actually interact with our tables.
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Making a 'view' of all state objects"""
    db_user = sys.argv[1] if len(sys.argv) > 1 else 'root'
    db_passwd = sys.argv[2] if len(sys.argv) > 2 else 'root'
    db_name = sys.argv[3] if len(sys.argv) > 3 else 'hbtn_0e_6_usa'
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(db_user, db_passwd, db_name),
        # echo=True,  # Activates "verbose mode" for engine
        pool_pre_ping=True
    )

    # More in-depth verification of what actually exist
    # inspector = inspect(engine)
    # tables = inspector.get_table_names()
    # print(f"Tables existing in :{db_name}", tables)

    # Create a Session class which can then "spawn" transactional objects.
    Session = sessionmaker(bind=engine)
    # Create a new "channel" to query database.
    states_reader = Session()
    for state in states_reader.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
