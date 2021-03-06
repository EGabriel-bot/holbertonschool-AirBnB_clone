#!/usr/bin/python3
"""Defines the User class."""
from mimetypes import init
from models.base_model import BaseModel


class User(BaseModel):
    """ Represents user info.

        Inherits from BaseModel.

        Attributes:
        email: The users email.
        password: The users password.
        first_name: The users first name.
        last_name: The users last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
