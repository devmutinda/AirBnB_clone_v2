#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine

class DBStorage:
    """This class manages storage of hbnb models"""
    __engine = None
    __session = None
#env variables
    def.__init__(self):
        self.__engine = create_engine(' mysql+mysqldb://{}:{}@{}/{}', \
                                        format(user,passwd,host,db), pool_pre_ping=True)
