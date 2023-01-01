#!/usr/bin/python3
"""This module defines the class 'FileStorage'."""
import json
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances."""
    __file_path = ''  # path to the JSON file
    __objects = {}    # will store all objects by <class name>.id

    def __init__(self):
        """constructor."""

    def all(self):
        """returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in '__objects' the 'obj' with key <obj class name>.id"""
        
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file."""

        full_name = os.path.join(FileStorage.__file_path, 'file.json')
        
        with open(full_name, 'w', encoding='UTF-8') as fp:
            json.dump(FileStorage.__objects, fp, indent = 4)

    def reload(self):
        """deserializes the JSON file to __objects if __file_path
        exists."""
        
        path = FileStorage.__file_path + 'file.json'
        if os.path.isfile(path):
            with open(path, 'r', encoding='UTF-8') as fp:
                FileStorage.__objects = json.load(fp)
