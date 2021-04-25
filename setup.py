#!/usr/bin/env python

from distutils.core import setup
from glob import glob
from os.path import splitext, basename

from setuptools import find_packages

setup(name='Backend-Proyectos',
      version='1.0',
      description='Backend de Seedtfiuba',
      author='Grupo 5',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
     )