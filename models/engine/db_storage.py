#!/usr/bin/python3
""" Module for db storage engine """
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    """ Database storage class """
    __engine = None
    __session = None

    def __init__(self):
        """ Custom init method """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        mode = os.getenv('HBNB_ENV')

        print("init db")
        DBStorage.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{database}",
            pool_pre_ping=True)


    def all(self, cls=None):
        """ Returns objects stored in db """
        if cls:
            res = self.__session.query(cls)
        else:
            res = self.__session.query(
                BaseModel, User, Place,
                State, City, Amenity, Review)
        
        return res

    def new(self, obj):
        """ Adds object to session """
        if obj is None:
            return
        DBStorage.__session.add(obj)

    def save(self):
        """ Commits current changes in session """
        DBStorage.__session.commit()

    def reload(self):
        """ Reloads """
        session_factory = sessionmaker(
            bind=DBStorage.__engine,
            expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session()
        Base.metadata.create_all(DBStorage.__engine)



