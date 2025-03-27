from setuptools import setup, find_packages

setup(
    name='token_refresh',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        "requests",
        "dotenv"
    ],
    author="Fernando Favaro Bonetti",
    url="https://github.com/Fernando0FB/token-refresh"
)