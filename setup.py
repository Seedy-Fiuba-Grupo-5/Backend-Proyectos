#!/usr/bin/env python

from distutils.core import setup
from glob import glob

from setuptools import find_packages

setup(name='Backend-Proyectos',
      version='1.0',
      description='Backend de Seedtfiuba',
      author='Grupo 5',
      packages=find_packages('src'),
      package_dir={'': 'src'},
     )