#!/usr/bin/python3
"""Instantiates storage object."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
