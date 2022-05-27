#!/usr/bin/python
""" holds class Post"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Post(BaseModel, Base):
    """Representation of Post """
    if models.storage_t == "db":
        __tablename__ = 'posts'
        owner = Column(String(60), ForeignKey('users.id'), nullable=False)
        post = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
