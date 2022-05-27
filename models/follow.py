#!/usr/bin/python
""" holds class Like"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Follow(BaseModel, Base):
    """Representation of Like """
    if models.storage_t == "db":
        __tablename__ = 'follow'
        followId = Column(String(60), ForeignKey('users.id'), nullable=False)
        followingId = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        print("** input values **")

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
