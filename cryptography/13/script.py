#! /usr/bin/python3

f = open('encrypted', 'r')

cipher = f.readline()

print(cipher)

dec = 13

for c in cipher :
    if ((ord(c) >= 97) and (ord(c) <= 122)):
        tmp = (ord(c) + dec)
        if tmp > 122 :
            print(chr((tmp % 123) + 97), end="")
        else :
            print(chr(tmp), end="")
    elif ((ord(c) >= 65) and (ord(c) <= 90)) :
        tmp = (ord(c) + dec)
        if tmp > 90 :
            print(chr((tmp % 91) + 65), end="")
        else :
            print(chr(tmp), end="")
    else:
        print(c, end="")