#!/usr/bin/python3
"""Defines a amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents a amenity.

        inherits from BaseModel
        Attributes:
            name: Name of the amenity.
    """
    name = ""
