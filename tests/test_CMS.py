import pytest
import os
from pathlib import Path
from CMS import getconfig

def test_getconfig():
    assert getconfig() != None, 'Config is empty'

def test_getconfig_locale_not_null():
    assert getconfig()['settings']['locale'] != None, 'Locale is not set'