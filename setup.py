from setuptools import find_packages, setup
from os import path


HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="vectortoolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="vectortoolkit"),
    package_dir={"": "vectortoolkit"},
    version="0.1.0",
    description="3D vector toolkit for Lambda Automata",
    author="Alex A",
    install_requires=[]
)