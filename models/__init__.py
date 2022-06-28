#!/usr/bin/env python3
"""Instantiates a storage object."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()