#!/usr/bin/python
""" holds class Like"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Comment(BaseModel, Base):
    """Representation of comments """
    if models.storage_t == "db":
        __tablename__ = 'comments'
        userId = Column(String(60), ForeignKey('users.id'), nullable=False)
        post = Column(String(60), ForeignKey('posts.id'), nullable=False)
        comment = Column(String(128),nullable=False)
    else:
        print("** input values **")

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
