#!/usr/bin/env python3
"""Defines a amenity class."""
import models
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represents a amenity.

        inherits from BaseModel
        Attributes:
            name: Name of the amenity.
    """
    name = ""