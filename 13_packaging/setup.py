from distutils.core import setup

from setuptools import find_packages
from calculator import version

from cx_Freeze import setup, Executable

setup(
    name='calculator',
    version=version,
    packages=find_packages(exclude=['tests']),
    install_requires=['requests'],
    url='http://jeff.com',
    license='MIT',
    author='Jeff Stevens',
    author_email='jeff@example.com',
    description='',

)
