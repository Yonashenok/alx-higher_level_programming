#!/usr/bin/python3
#base.py
"""Defines class"""
class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize a new base
        arg:
        id (int)
        """
        if id is not None and type(id) == int:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
