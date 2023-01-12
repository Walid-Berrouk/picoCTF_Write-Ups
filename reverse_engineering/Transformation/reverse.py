#! /usr/bin/python3

f = open('./enc')

reversed_flag = f.read()
flag = ""

# My Attempt
for i in reversed_flag :
    flag += chr(int(bin(ord(i))[2:-8], base = 2))  + chr(int(bin(ord(i))[-8:], base = 2))

# Write Up Solution
# for i in range(len(reversed_flag)):
#     flag += chr(ord(reversed_flag[i])>>8) + chr((ord(reversed_flag[i]))-((ord(reversed_flag[i])>>8)<<8))

print(flag)