#!/usr/bin/python3
"""
    Defines unittests for models/base_model.py.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""
