#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import storage
from models.engine.db_storage import DBStorage
# from os import getenv


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
            for obj in storage.all(City).values():
                if self.id == obj.id:
                    city_list.append(obj)

            return city_list
