#!/usr/bin/python3
from plistlib import UID
import uuid


class BaseModel:
    uid = uuid.uuid4()
    u_id = str(uid)

    def __init__(self, id, created_at, updated_at):
        self.id = u_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
