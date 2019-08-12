#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base




class City(Base):
    """City Class"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_Key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
