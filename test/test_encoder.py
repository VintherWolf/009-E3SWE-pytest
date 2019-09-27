# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:58:54 2019

@author: danie
"""

import pytest

from src import encoder

pytest

def testEncoder():
    assert encoder.encode('aa') == '2a'
    assert encoder.encode('eeee') == '3e'
    