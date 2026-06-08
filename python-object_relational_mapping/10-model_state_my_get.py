#!/usr/bin/python3
"""Returns all States having a 'a' in their name"""

# For details on why each import please confer previous task.
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func  # Required to guarantee case-sensitive LIKE.


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
    state_searcher = Session()
    # Normally we'd check the argument far earlier
    state_to_search = sys.argv[4] if len(sys.argv) > 4 else "Texas"

    matching_state = (
        state_searcher.query(State)
        # Needing to use .filter(func.binary) instead of just .like()
        #   because the latter does not guarantee case-sensitive behaviour.
        .filter(State.name == state_to_search)
        .first()  # Chosen since task seem to hint always only 1 result.
    )

    if matching_state is None:
        print("Not found")
    else:
        print(matching_state.id)
    # Preferred over session.query(State).order_by(State.id).limit(1).all()
    #  because the latter would return a list whatever the limit number is
    #  (and whether or not there are actual results) thus forcing the use
    #  of a loop to manually "unwrap" each element.
