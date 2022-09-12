#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String

class City(Base, BaseModel):
    """ The city class, contains state ID and name """
    # state_id = ""
    # name = ""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey('state.id'))
    #those db and fs connections at the end not found resources yet