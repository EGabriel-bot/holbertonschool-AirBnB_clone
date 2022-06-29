#!/usr/bin/env python3
"""Defines a city class."""
import models
from models.base_model import BaseModel

class City(BaseModel):
    """Represents a city.

        inherits from BaseModel
        Attributes:
            state_id: Name of state.
            name: Name of the city.
    """
    state_id = ""
    name = ""
