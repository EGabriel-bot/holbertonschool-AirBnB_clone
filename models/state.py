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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
