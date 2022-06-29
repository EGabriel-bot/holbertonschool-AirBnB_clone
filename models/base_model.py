#!/usr/bin/env python3
"""Defines a BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines a BaseModel class.

    Attributes:
        created_at: The datetime at creation.
        updated_at: The datetime of last update.
        """

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v, in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        """Returns the print/str representation of the BaseModel"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
