#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """create a relationship for state in Filestorage"""
        Cities = []
        cityinstance = storage.all(City)
        for city in cityinstance:
            if city["id"] == self.id:
                Cities.append(city)
        return ()
