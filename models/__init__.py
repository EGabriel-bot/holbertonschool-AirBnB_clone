#!/usr/bin/python3
"""
    Creation of storage variable as an instance of the FileStorage class.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
