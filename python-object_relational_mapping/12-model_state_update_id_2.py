#!/usr/bin/python3
"""Changes state of id 2 to 'New Mexico'"""

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

    state_changer = Session()
    target_state_id = 2
    new_name = "New Mexico"

    # Session object silently starts a SQL "Transaction" but does NOT commit.
    state_to_update = state_changer.query(State).filter(State.id == 2).first()
    # Alternative syntax
    # state_to_update = state_changer.query(State).filter_by(id=2).first()
    state_to_update.name = new_name
    # print(state_to_update.name)
    state_changer.commit()
