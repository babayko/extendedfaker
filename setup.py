from distutils.core import setup


setup(
    name='extended-faker',
    version='0.0.1a',
    packages=['src.extended_faker', 'src.extended_faker.providers',
              'src.extended_faker.providers.person',
              'src.extended_faker.providers.person.ru_RU'],
    url='',
    license='MIT',
    author='babay',
    author_email='',
    description='Additional providers for fake-factory'
)
