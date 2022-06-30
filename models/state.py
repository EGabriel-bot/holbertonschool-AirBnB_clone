#!/usr/bin/env python3
"""Defines a state class."""
import models
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.

        inherits from BaseModel
        Attributes:
            name: Name of the state.
    """
    name = ""
