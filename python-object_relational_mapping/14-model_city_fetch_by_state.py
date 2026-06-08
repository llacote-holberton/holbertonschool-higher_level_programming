#!/usr/bin/python3
"""Printing all cities from 14 db"""

# For details on why each import please confer previous task.
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func  # Required to guarantee case-sensitive LIKE.
from model_city import City


if __name__ == "__main__":
    """Printing all cities's informations"""
    db_user = sys.argv[1] if len(sys.argv) > 1 else 'root'
    db_passwd = sys.argv[2] if len(sys.argv) > 2 else 'root'
    db_name = sys.argv[3] if len(sys.argv) > 3 else 'hbtn_0e_14_usa'
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(db_user, db_passwd, db_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)

    query_session = Session()
    # No need to precise an "ON" clause because there is only
    # one primary to foreign key relationship.
    # cities = query_session.query(State).join(City).all()
    # But I like being explicit anyways. :)
    states_and_cities = (
        query_session.query(State, City)
        .join(City, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )  # Will return tuples with (state, city) inside

    for state, city in states_and_cities:
        info_template = "{s_name}: ({c_id}) {c_name}"
        print(info_template.format(
            s_name=state.name,
            c_id=city.id,
            c_name=city.name
            )
        )
