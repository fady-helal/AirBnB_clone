#!/usr/bin/python3
"""
BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

    def save(self):
        """"""
        self.updated_at = datetime.utcnow()

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )

    def to_dict(self):
        """"""
        _dict = self.__dict__.copy()
        _dict["__class__"] = self.__class__.__name__
        _dict["created_at"] = self.created_at.isoformat()
        _dict["updated_at"] = self.updated_at.isoformat()
        return _dict
