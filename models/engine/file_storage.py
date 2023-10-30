#!/usr/bin/python3
"""This module creates a file storage class"""

import models
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes/deserializes json files"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns object dictionary"""

        return self.__objects

    def new(self, obj):
        """sets in object the obj with class name.id"""

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes objects to json file 'my_file'"""
        new_dict = {}

        with open(self.__file_path, "w+", encoding="utf-8") as f:
            for k, v in self.__objects.items():
                new_dict[k] = v.to_dict()
                json.dump(new_dict, f)

    def reload(self):
        """converts json file to objects"""

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                new_object = json.load(f)
                for k, v in new_object.items():
                    reloaded_obj = eval("{}(**v)".format(v["__class__"]))
                    self.__objects = reloaded_obj

        except IOError:
            pass
