from setuptools import find_packages, setup

setup(
    name="vectortoolkit",
    packages=find_packages(where="vectortoolkit"),
    package_dir={"": "vectortoolkit"},
    version="0.1.0",
    description="3D vector toolkit for Lambda Automata",
    author="Alex A",
    install_requires=[]
)