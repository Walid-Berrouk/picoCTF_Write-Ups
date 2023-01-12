#! /usr/bin/python3

from pwn import *

# nc saturn.picoctf.net 51109
HOST = 'saturn.picoctf.net'
PORT = 51109

target = remote(HOST, PORT)

preformated_flag =  target.recv().decode('UTF-8')[:-2] 

exec("print(" + preformated_flag + ")")
