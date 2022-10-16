#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
    name = Column(String(128), nullable=False)
