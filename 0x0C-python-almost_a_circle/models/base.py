#!/usr/bin/python3
"""this module defines the fundation class Base
"""
import json
import os


class Base:
    """class will be the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a JSON file.

        Args:
            cls: The class itself.
            list_objs (list): A list of instances to save to a file.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Save a list of instances to a JSON file.

        Args:
            cls: The class itself.
            list_objs (list): A list of instances to save to a file.

        Returns:
            None
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)
            else:
                obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """returns the list of the JSON string representation json_string"""
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_dict = cls.from_json_string(list_str)

        return [cls.create(**d) for d in list_dict]
