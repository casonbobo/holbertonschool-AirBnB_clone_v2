#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy import relationship
from models.base_model import BaseMode, Base
from models.city import City



class State(BaseModel):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")

    if models.storage_type != "db":
        @property
        def cities(self):
            """ getter attribute that returns the list of City instances """
            all_cities = models.storage.all(City)
            state_cities = []
            for city in all_cities.values():
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
