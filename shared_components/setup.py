# pylint: disable=import-error
from setuptools import setup, find_packages


setup(
    name='shared_db_connection',
    version='0.1.0', 
    packages=find_packages(),
    description='shared database connection',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Sultan'
)