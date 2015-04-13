# coding: utf-8
from unittest import TestCase
from factory import Factory


class TestFactory(TestCase):
    def test_create(self):
        faker = Factory.create()
        result = faker.marriage_status()
        result = faker.male_nation()
        pass