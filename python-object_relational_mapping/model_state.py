#!/usr/bin/python3
"""Creates a MySQL database model with SQLAlchemy"""


# Confer https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# and ./en/13/orm/extensions/declarative/basic_use.html
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Model of a db table storing infos about country states"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
