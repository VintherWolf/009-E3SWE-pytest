# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:00:32 2019

@author: Daniel Korsgaard Vinther Wolf
Comment: Implementation from Anders Lehmann (AU-Herning)
"""

def encode(mess):
    ''' Run Length Encoding - konverter strenge
        fra 'wwwwwwwbbbb' '6w4b' '''
    res = []
    old = mess[0]
    i = 0
    for c in mess:
        if c == old:
            i += 1
        else:
            res.append('%d%c' % (i,c))
            old = c
            i = 1
    res.append('%d%c' % (i,c))
    return ''.join(res)

def decoder(mess):
    return ''