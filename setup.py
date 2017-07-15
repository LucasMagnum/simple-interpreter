#!/usr/bin/env python

from distutils.core import setup

import interpreter


setup(
    name='Simple interpreter',
    version=interpreter.__version__,
    description='Simple interpreter for Pascal language.',
    author='Lucas Magnum',
    author_email='lucasmagnumlopes@gmail.com',
    packages=['interpreter'],
)
