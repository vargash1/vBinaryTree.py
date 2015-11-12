#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: vargash1
# @Date:   2015-11-11 03:42:08
# @Email:  vargash1@wit.edu
# @Name :  Vargas, Hector
# @Last Modified by:   vargash1
# @Last Modified time: 2015-11-12 03:33:57
import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "vbinarytree",
    version = "0.0.0",
    author = "Hector Vargas",
    author_email = "hjvargas1213@gmail.com",
    description = ("A simple implementation of a Binary Tree "
                    "along with some useful methods."),
    license = "MIT",
    keywords = "example documentation simple bst",
    url = "https://github.com/vargash1/vBinaryTree.py",
    packages=['vbt'],
    long_description=read('README.md')
)