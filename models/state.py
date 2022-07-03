#!/usr/bin/python3
"""Defines a state class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.

        inherits from BaseModel
        Attributes:
            name: Name of the state.
    """
    name = ""
