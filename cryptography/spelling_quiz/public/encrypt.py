#! /usr/bin/python3

import random
import os

files = [
    os.path.join(path, file)
    for path, dirs, files in os.walk('.')
    for file in files
    if file.split('.')[-1] == 'txt'
]

alphabet = list('abcdefghijklmnopqrstuvwxyz')
random.shuffle(shuffled := alphabet[:])
# dictionary = dict(zip(alphabet, shuffled))

# After a Substituion attack using this website : https://www.dcode.fr/monoalphabetic-substitution
# See Also :
# https://mathweb.ucsd.edu/~crypto/java/EARLYCIPHERS/Monoalphabetic.html
# https://mathweb.ucsd.edu/~crypto/java/EARLYCIPHERS/breakmono.html

# Got this Reciprocial Substitution

dictionary = {
    'a': 's',
    'b': 'p',
    'c': 'r',
    'd': 'g',
    'e': 'w',
    'f': 'h',
    'g': 'k',
    'h': 'j',
    'i': 'o',
    'j': 'q',
    'k': 'z',
    'l': 'l',
    'm': 'd',
    'n': 'c',
    'o': 'u',
    'p': 'v',
    'q': 'y',
    'r': 'e',
    's': 'm',
    't': 'n',
    'u': 'b',
    'v': 't',
    'w': 'i',
    'x': 'a',
    'y': 'f',
    'z': 'x'
}

for filename in files:
    text = open(filename, 'r').read()
    encrypted = ''.join([
        dictionary[c]
        if c in dictionary else c
        for c in text
    ])
    open(filename, 'w').write(encrypted)
