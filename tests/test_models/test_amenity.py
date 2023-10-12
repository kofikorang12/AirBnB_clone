#!/usr/bin/env python3
''' unit testing for Amenity class '''

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    ''' class for testing Amenity '''

    def test_attribute_creation(self):
        ''' testing instance initializes with attribute '''
        a = Amenity()
        self.assertEqual(type(a.name), str)
