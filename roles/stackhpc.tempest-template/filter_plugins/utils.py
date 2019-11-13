from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from functools import partial
import types
from ansible.module_utils import six

from ansible import errors
from os import path


def exists(p):
    return path.exists(p)

# ---- Ansible filters ----
class FilterModule(object):
    ''' General Utilities '''
    filter_map = {
        'exists': exists,
    }

    def filters(self):
        return self.filter_map