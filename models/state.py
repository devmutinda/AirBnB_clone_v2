#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    # name = ""
     __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="all, delete")

    @property
    def cities(self):
        """returns the list of City instances"""
        from models import storage
        new_list = []
        # storage.reload()
        all_obj = storage.all(City)
        for value in all_obj.values():
            if value['state_id'] == self.id:
                new_list.append(value['name'])

        return new_list
