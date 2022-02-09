# -*- encoding: utf-8 -*-

import os
import sys
import json
import functools
import operator

translations_path = os.getcwd()
selected_extension = ".lang"
translations = []

"""
Author: Disk_MTH
GitHub: https://github.com/Disk-MTH/Python-package-template
License: MIT

For more information about the usage of this library read the full documentation at :
        https://github.com/Disk-MTH/Python-package-template/blob/master/diskmth/README.md
"""


def print_hello():
    print("Hello world!")
