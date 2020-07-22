"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['AmbientMusicForUniversities.py']
DATA_FILES = ['./audioEngine/abs_dly_short_vd1.pd', './audioEngine/abs_fm_op1.pd', './audioEngine/abs_moddelayline1.pd',
              './audioEngine/rev2~.pd', './audioEngine/two_ops1poly.pd']
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)