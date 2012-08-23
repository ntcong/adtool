# -*- coding: utf-8 -*-
from distutils.core import setup
import sys
import py2exe
from py2exe.build_exe import py2exe
import os
sys.argv.append('py2exe')

setup(
    name='adtool',
    version='1.0',
    author='CongNT3',
    windows=[{"script": "adtool.py", 'icon_resources':[(1, 'adtool.ico')]}],
    options={"py2exe":
                {"dll_excludes": ["mswsock.dll", "powrprof.dll", "IPHLPAPI.DLL", "packet", "MSVCP90.dll"],
                    "excludes": ["pywin", "pywin.debugger", "_ssl", "doctest", "pdb",
                                "unittest", "difflib", "inspect", "pyreadline", 'optparse',
                                'pickle', 'calendar', 'locale'],
                    "packages": ["win32api"],
                 #"includes":["sip"],
                 'bundle_files': 3,
                 'optimize': 2,
                 "compressed": 1,

                }},
    zipfile=None,

        )
