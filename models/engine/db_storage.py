#!/usr/bin/python3
"""
Contain the class DBStorage
"""

import models
from os import getenv
from models.BaseModel import BaseModel, Base
from sqlalchemy import create_engine


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
