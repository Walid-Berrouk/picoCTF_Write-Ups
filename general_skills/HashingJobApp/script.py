#! /usr/bin/python3

from pwn import *
import hashlib

# nc saturn.picoctf.net 51109
HOST = 'saturn.picoctf.net'
PORT = 57689

target = remote(HOST, PORT)

while True :

    str_to_hash = target.recv()

    try:
        str_to_hash = str_to_hash.decode('UTF-8').replace('\r\n', '').split("'")[1]

        target.sendline(hashlib.md5(str_to_hash.encode()).hexdigest())

        print(target.recvline())
        print(target.recvline())

    except:
        print(str_to_hash)
        break
