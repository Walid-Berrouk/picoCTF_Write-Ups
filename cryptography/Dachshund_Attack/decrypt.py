#! /usr/bin/python3

from Crypto.Util.number import *
import owiener

f = open('output.txt', 'r')
e = int(f.readline().split(":")[1])
n = int(f.readline().split(":")[1])
c = int(f.readline().split(":")[1].strip())


# Decryption with brute force (Doesn't Work)
# for d in range(9999999) :
#     flag = long_to_bytes(pow(int(c), d, int(n)))
#     if b"picoCTF{" in flag :
#         print(f"Decrypted flag : {flag}")

# Decryption with weiner Attack
d = owiener.attack(e, n)

if d is None:
    print("Failed")
else:
    print("Hacked d={}".format(d))
    flag = long_to_bytes(pow(c, d, n))
    print(f"Decrypted flag : {flag}")