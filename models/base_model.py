#!/usr/bin/python3
import uuid
from datetime import datetime
import time


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()


test = BaseModel()
print(test.updated_at)
time.sleep(5)
test.save()
print(test.updated_at)
