#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """This class manages storage of hbnb models"""
    __engine = None
    __session = None
    # env variables
    def __init__(self):
        """Constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv(HBNB_MYSQL_USER),
                                             getenv(HBNB_MYSQL_PWD),
                                             getenv(HBNB_MYSQL_HOST),
                                             getenv(HBNB_MYSQL_DB)),
                                      pool_pre_ping=True)
        if getenv(HBNB_ENV) == "test":
            Base.metadata.drop_all(self.__engine)
