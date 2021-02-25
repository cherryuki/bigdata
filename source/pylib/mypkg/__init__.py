# -*- coding: utf-8 -*-
"""mypkg/__init__.py
"""
try:
    import os
    import _mypkg_foo
    __path__.append(os.path.abspath(os.path.dirname(_mypkg_foo.__file__)))
except ImportError:
    print("_mypkg_foo import error")

print("mypkg import됨")