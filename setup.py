from setuptools import find_packages
from setuptools import setup


def readme():
    with open("README.md") as readme:
        return readme.read()


setup(
    name="pyiocontrol",
    version="0.0.2",
    description="iarduino.ru module for Raspberry Pi",
    long_description=readme(),
    classifiers=["Programming Language :: Python :: 3"],
    url="http://github.com/tremaru/pyiocontrol",
    author="iarduino.ru",
    author_email="shop@iarduino.ru",
    include_package_data=True,
    packages=find_packages(exclude=("tests",)),
    license="MIT",
    install_requires=["requests==2.23.0"],
)
