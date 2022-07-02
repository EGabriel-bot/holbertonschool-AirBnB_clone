#!/usr/bin/python3
"""Defines a review class."""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.

        inherits from BaseModel
        Attributes:
            place_id: string containing the Place ID.
            user_id: string containing the User ID.
    """
    place_id = ""
    user_id = ""
    text = ""
