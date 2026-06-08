#!/usr/bin/python3
"""Reads info from States table using Alchemy ORM as interface"""

# For details on why each import please confer previous task.
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
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

    # Create a Session class which can then "spawn" transactional objects.
    Session = sessionmaker(bind=engine)
    # Create a new "channel" to query database.
    states_reader = Session()
    # I choose to go for "ORDER + LIMIT" in case table evolves and "1"
    #   ends up being removed (hence not the "first" anymore)
    first_state = states_reader.query(State).order_by(State.id).first()
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")
    # Preferred over session.query(State).order_by(State.id).limit(1).all()
    #  because the latter would return a list whatever the limit number is
    #  (and whether or not there are actual results) thus forcing the use
    #  of a loop to manually "unwrap" each element.
