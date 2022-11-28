#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from models import storage
from models.engine.db_storage import DBStorage


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)


    if type(storage) is not DBStorage:

        @property
        def cities(self):
            """Gets current cities from state"""
            from models.city import City

            city_list = []
            for key, val in storage.all(City).items():
                city_list.append(val)

            return city_list
