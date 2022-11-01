import os
import re
from io import open

from django.templatetags.static import static

#
# This bit of code is used to import specific data settings from the .init.py file
#
class StaticWrapper:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return static(self.path)


def read(f):
    return open(f, 'r', encoding='utf-8').read()


def get_field(package, field):
    """
    Return field from `__init.py__`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("{0} = ['\"]([^'\"]+)['\"]".format(field), init_py).group(1)
