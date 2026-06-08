#!/usr/bin/python3
"""Delete states which have 'a' in name"""

# For details on why each import please confer previous task.
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func  # Required to guarantee case-sensitive LIKE.


if __name__ == "__main__":
    """Changing State 2's name to New Mexico"""
    db_user = sys.argv[1] if len(sys.argv) > 1 else 'root'
    db_passwd = sys.argv[2] if len(sys.argv) > 2 else 'root'
    db_name = sys.argv[3] if len(sys.argv) > 3 else 'hbtn_0e_6_usa'
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(db_user, db_passwd, db_name),
        # echo=True,  # Activates "verbose mode" for engine
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)

    states_eraser = Session()
    target_character = "a"

    states_to_delete = (
        states_eraser.query(State)
        .filter(func.binary(State.name).like(f"%{target_character}%"))
        .all()
    )
    for state in states_to_delete:
        states_eraser.delete(state)

    states_eraser.commit()
