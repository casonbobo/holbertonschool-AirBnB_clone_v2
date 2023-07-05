#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        """DB State class"""
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete")
    else:
        """File Storage State"""
        name = ""

        @property
        def cities(self):
            """Returns a list of cities equal to their state ID"""
            list_cities = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
