#! /usr/bin/python3

f = open('ciphertext', 'r')

cipher = f.readline().split('{')[1].split('}')[0]

print(cipher)

for i in range(26) :
    for c in cipher :
        tmp = (ord(c) + i)
        if tmp > 122 :
            print(chr((tmp % 123) + 97), end="")
        else :
            print(chr(tmp), end="")
    print()