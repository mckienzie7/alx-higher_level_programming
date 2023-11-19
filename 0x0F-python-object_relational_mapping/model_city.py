#!/usr/bin/python3
"""City class created"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class City(Base):
    """Class city"""
    __tablename__ = "cities"
    id = Column(
            Integer,
            autoincrement=True,
            unique=True,
            nullable=False,
            primary_key=True
            )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, foreign_key='states.id', nullable=False)
