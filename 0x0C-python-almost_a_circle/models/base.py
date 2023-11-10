#!/usr/bin/python3
"""Defines a class Base"""

import json
import csv


class Base:
    """
    A base class with one private class attribute and
    one instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialises once an instance is created"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(f'{cls.__name__}.json', 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            new_list = []
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
            f.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ return list of instances """
        new_list = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                new_list = cls.from_json_string(f.read())
            for i, j in enumerate(new_list):
                new_list[i] = cls.create(**new_list[i])
        except FileNotFoundError:
            pass
        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes in csv format"""
        filename = cls.__name__ + ".csv"
        if cls.__name__ is "Rectangle":
            attrs = ["width", "height", "x", "y", "id"]
        elif cls.__name__ is "Square":
            attrs = ["size", "x", "y", "id"]
        with open(filename, 'w', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=attrs)
            if list_objs is not None:
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
            else:
                writer.writerow([[]])

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes in csv format """
        filename = cls.__name__ + ".csv"
        new_list = []
        try:
            with open(filename, 'r', newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    for k, v in row.items():
                        row[k] = int(v)
                    new_list.append(row)
            return [cls.create(**obj) for obj in new_list]
        except FileNotFoundError:
            return [[]]
