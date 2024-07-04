#!/usr/bin/python3
"""Defined State class which inherits from Base class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Using declarative_base function to return a new base class
# Mapped class State will inherit from Base and generate new Table and mapper()
Base = declarative_base()

# Map class to inherit from Base
class State(Base):
    """Mapped class definition"""

    # Table
    __tablename__ = 'states'

    # Describe table, column objects, use methods imported from sqlalchemy
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
