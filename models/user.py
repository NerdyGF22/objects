import models
from models.BaseModel import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String,Integer
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Represation of the user"""

    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128),nullable = False)
        password = Column(String(128),nullable = False)
        fullname = Column(String(128),nullable = False)
        bio = Column(String(128),nullable = False)
        profilepicture = Column(String(128),nullable = False)
        coverpicture = Column(String(128),nullable = False)
    else:
        __tablename__ = 'users'
        email = Column(String(128),nullable = False)
        password = Column(String(128),nullable = False)
        fullname = Column(String(128),nullable = False)
        bio = Column(String(128),nullable = False)
        profilepicture = Column(String(128),nullable = False)
        coverpicture = Column(String(128),nullable = False)
    
    def __init__(self, *args, **kwargs):
        """ initializes users"""
        super().__init__(*args, **kwargs)