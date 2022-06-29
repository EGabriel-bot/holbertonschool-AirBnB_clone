#!/usr/bin/env python3
"""Defines a place class."""
import models
from models.base_model import BaseModel

class Place(BaseModel):
    """Represents a place.

        inherits from BaseModel
        Attributes:
            city_id:
            user_id:
            name: Name of the city.
            description:
            number_rooms:
            number_bathrooms:
            max_guest:
            price_by_night:
            latitude:
            amenity_ids:
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0.0
    latitude = 0.0
    amenity_ids = []
