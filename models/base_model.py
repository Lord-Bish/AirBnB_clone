#!/usr/bin/python3
"""
This module creates a Basemodel that defines all class attributes
"""

import models
import uuid
from datetime import datetime

class BaseModel():
    """Defines all class attributes"""

    def __init__(self, *args, **kwargs):
        """Initializes all instance attributes"""

        if len(kwargs) != 0:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """prints string representaion of objects"""

        return (f"{self.__class__.__name__} {self.id} {self.__dict__}8")

    def save(self):
        """updates updated_at with current datetime"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dictionary key/values of instances"""

        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        return (mydict)