#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from models.base_model import Base, BaseModel


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
