# coding: utf-8

from faker import Factory as BaseFactory
from providers.person.ru_RU import Provider as PersonProvider


class Factory(BaseFactory):
    """
    Расширенный класс с дополнительными провайдерами
    """

    @classmethod
    def create(cls, **kwargs):
        faker = super(Factory, cls).create(**kwargs)
        faker.add_provider(PersonProvider)

        return faker