#!/usr/bin/python3
"""This module defines the class 'FileStorage'."""
import json
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances."""
    __file_path = 'file.json'  # path to the JSON file
    __objects = {}    # will store all objects by <class name>.id

    def all(self):
        """returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in '__objects' the 'obj' with key <obj class name>.id"""

        key = '{}.{}'.format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def classes(self):
        """Returns a dictionary of valid classes - for the serialization-
        deserialization process."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "Place": Place,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Review": Review
                   }
        return classes

    def save(self):
        """serializes __objects to the JSON file."""

        obj_dict = FileStorage.__objects.copy()

        for key, val in obj_dict.items():
            obj_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as fp:
            json.dump(obj_dict, fp, indent=4)

    def reload(self):
        """loads storage dictionary from file."""

        rel_dict = {}
        path = FileStorage.__file_path

        if os.path.isfile(path):
            with open(path, 'r', encoding='UTF-8') as fp:
                rel_dict = json.load(fp)

        for key, val in rel_dict.items():
            class_name = key.split('.')[0]
            FileStorage.__objects[key] = self.classes()[class_name](**val)
