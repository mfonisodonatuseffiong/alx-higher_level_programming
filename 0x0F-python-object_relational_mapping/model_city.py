#!/usr/bin/python3
""" City Model """

from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base  # Assuming Base is imported from model_state

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    def __repr__(self):
        return f"City(id={self.id}, name={self.name}, state_id={self.state_id})"
