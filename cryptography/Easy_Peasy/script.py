#! /usr/bin/python3

from pwn import *
from binascii import unhexlify

HOST = 'mercury.picoctf.net'
PORT = 20266

p = remote(HOST, PORT)

# First prints
p.recvline()
p.recvline()
encrypted_flag = p.recvline().strip()
bin_encrypted_flag =  unhexlify(encrypted_flag)

exploit = "a"*(50000 - len(bin_encrypted_flag))

p.sendlineafter(b'What data would you like to encrypt? ', exploit.encode())
p.sendlineafter(b'What data would you like to encrypt? ', bin_encrypted_flag)
p.recvline()
print("The Flag is : " + unhex(p.recvline().strip()).decode())
p.interactive()
