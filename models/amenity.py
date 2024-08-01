#!/usr/bin/python3
"""This is the amenity Class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
import os
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This is the Class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False, default="")
        place_amenities = relationship(
            "Place", secondary=place_amenity)
    else:
        name = ""
