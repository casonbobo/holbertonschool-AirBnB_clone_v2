#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
import models 


"""if city alredy exists with state id and name"""
if models.storage_type == "db":
    class City(BaseModel):
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states_id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
else:
    """or if it doesn't"""
    class City(BaseModel):
        state_id = ""
        name = ""
