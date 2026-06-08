#!/usr/bin/python3
"""Definition of a City model to integrate through SQLAlchemy"""


# Confer https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# and ./en/13/orm/extensions/declarative/basic_use.html
from sqlalchemy import Column, Integer, String
from model_state import Base
from sqlalchemy import ForeignKey        # Required for relationships
# from sqlalchemy.orm import relationship  # Required for better relationships


class City(Base):
    """Model of a db table storing infos about cities"""
    __tablename__ = "cities"
    # Note: technically autoincrement is implicit when Integer + Primary_key
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    # NOTE: if tables created from SQLAlchemy, states must be done
    #   before cities, but SQLAlchemy will manage that automatically
    #   with create_all as long as both classes are imported before.

    # Alternative to explicit joins when exploiting tables,
    #   useful if use of both cities and states would be frequent
    # Confer https://docs.sqlalchemy.org/en/13/orm/
    #   tutorial.html#building-a-relationship
    # Would require this (optional)
    # state = relationship("State", back_populates="cities")
    # AND adding this in the State model (mandatory)
    # cities = relationship("City", back_populates="state",
    #   order_by="City.id")
    # Back_populates makes SQLAchemy updates the relationships in memory only
    #   even before/without explicit commit() and new select.
