#!/usr/bin/python3

from pwn import xor
from random import randint

# Or

def encrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt



# Test 1

# print(encrypt(b"hello there", b"jkolp"))
# print(encrypt(b"hello there", b"jkolp"))
# print(encrypt(b"hello there", b"jkolp"))

# Result

# b'\x02\x0e\x03\x00\x1fJ\x1f\x07\t\x02\x0f'
# b'\x02\x0e\x03\x00\x1fJ\x1f\x07\t\x02\x0f'
# b'\x02\x0e\x03\x00\x1fJ\x1f\x07\t\x02\x0f'


# Test 2 

# print(encrypt(b"hello there", b'\x02\x0e\x03\x00\x1fJ\x1f\x07\t\x02\x0f'))

# Result

# b'jkolpjkolpj'


# Function to Decrypt after generating possibility
def Decrypt(arr, n):
    # Decryption
    with open('output.txt', 'rb') as f:
        output = f.read()

        # Extract only hexed part as we stringify it, and fromhex the output
        # output = bytearray.fromhex(str(str(output)[2:-1]))
        output = bytes.fromhex(str(output)[2:-1])

        # print(output)

    random_strs = [
        b'my encryption method',
        b'is absolutely impenetrable',
        b'and you will never',
        b'ever',
        # b'ever',
        # b'ever',
        # b'ever',
        # b'ever',
        # b'ever',
        b'break it'
    ]


    # Brute force to get the key
    # Apply xor on using each random strings
    for i in range(0, n):
        if arr[i] == 1 :
            output = encrypt(output, random_strs[i])

    cipher = output
    # Apply xor on final product to extract the key using a knwon strign
    output = encrypt(output, b'picoCTF{')

    # key
    # print(output[0:7])

    flag = encrypt(cipher, output[0:7])
    if flag.startswith(b'picoCTF{'):
        print("key :", str(output)[2:9])
        print(str(flag)[2:-1])

 
# Function to generate all binary strings
def generateAllBinaryStrings(n, arr, i):
 
    if i == n:
        Decrypt(arr, n)
        return
     
    # First assign "0" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)
 
    # And then assign "1" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)

# Driver Code
if __name__ == "__main__":
 
    n = 5
    arr = [None] * n
 
    # Print all binary strings
    generateAllBinaryStrings(n, arr, 0)
