# pylint: disable=import-error
from setuptools import setup, find_packages


setup(
    name="shared_db_connection",
    version="0.1.5",
    packages=find_packages(),
    description="shared database connection",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sultan",
    url="https://github.com/mcnugets/ubi.git@database_connection",
    install_requires=[
        "sqlalchemy>=1.4.0,",
        "pydantic>=1.7.1",
        "python-dotenv>=0.17.0",
        "alembic>=1.12.1"
    ],
    include_package_data=True
)
