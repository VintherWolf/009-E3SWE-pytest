# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:00:32 2019

@author: Daniel Korsgaard Vinther Wolf
Comment: Implementation from Anders Lehmann (AU-Herning)
"""

from time import sleep

class MyException(Exception):
    pass

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

def decode(mess):
    res = ''
    count = 0
    for c in mess:
        if c.isdigit():
            count = count*10 + int(c)
        else:
            res += c*count
            count = 0
    return res

if __name__ == '__main__':
    import sys
    argv = sys.argv
    if '-e' in argv:
        filename = argv[argv.index('-e')+1]
        func = encode # func er en funktion. Her er det encode
    elif '-d' in argv:
        filename = argv[argv.index('-d')+1]
        func = decode # func er en funktion. Her er det decode
    else:
        filename = argv[-1]
        func = lambda x: decode(encode(x)) # func er en funktion. Her decode(encode(x))
    with open(filename,'r') as f:
        print(func(f.read()))
    # Denne pause er nødvendig for at fuzzeren kan skelne
    # mellem crash og succes (en fejl i fuzzzeren)
    sleep(2)
    exit(0)