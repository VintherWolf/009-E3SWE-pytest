# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:58:54 2019

@author: Daniel Korsgaard Vinther Wolf

"""

import pytest

from src import encode


def testEncoder():
    assert encode('aa') == '2a'
    assert encode('eeee') == '4e'

