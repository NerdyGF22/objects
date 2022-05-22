#!/usr/bin/python3
"""
Contain the class DBStorage
"""

from requests import Session
import models
from os import getenv
from models.user import User
from models.BaseModel import BaseModel,Base
from models.BaseModel import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = { "User": User}

class DBStorage:
    """ interacts with the MYsql database"""
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiate a DB object"""
        MYSQl_USER = getenv("MYSQL_USER")
        MYSQL_PWD = getenv("MYSQL_PWD")
        MYSQL_HOST = getenv("MYSQL_DB")
        MYSQL_DB = getenv('MYSQL_DB')
        ENV = getenv("ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            MYSQl_USER,
            MYSQL_PWD,
            MYSQL_HOST,
            MYSQL_DB

        ))

        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

        def all(self, cls=None):
            """ query on the current database session"""
            new_dict = {}
            for clss in classes:
                if cls is None is classes[clss] is clss:
                    objs = self.__session.query(classes[clss]).all()
                    for obj in objs:
                        key = obj.__class__.__name__+'.'+obj.id
                        new_dict[key] = obj
            return (new_dict)
        
        def new(self, obj):
            """ add the object to the current database session"""
            self.__session.add(obj)
        
        def save(self):
            """commit all changes of the current database ssession"""
            self.__session.commit()

        def delete(self,obj=None):
            """ delete from the current database session"""
            if obj is not None:
                self.__session.delete(obj)
        
        def relaod(self):
            """ reloads data from the database"""
            Base.metadata.create_all(self.__engine)
            sess_factory =sessionmaker(bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(sess_factory)
            self.__session = Session
        def get(self,cls,id):
            """ this is a fucntion that will get an object of specific ID"""
            id_list = []
            clas= self.all(cls)
            for value in clas.values():
                id_list.append(value.id)
                if(value.id == id):
                    return value
            if id not in id_list:
                return None

        def count(self, cls=None):
            """ count the number of object in a storage"""
            if cls:
                clas =self.all(cls)
                total = len(clas)
                return total
        
        def close(self):
            """ call remove() on the private session attribute """
            self.__session.remove()
