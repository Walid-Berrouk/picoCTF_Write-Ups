#! /usr/bin/python3

flag = "I'm a flag"

# print(''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))

for i in range(0, len(flag), 2) : 
    print(bin(ord(flag[i])))
    print(bin(ord(flag[i]) << 8))

# x << y
#     Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y. 

# Result 
# 0b1001001
# 0b100100100000000
# 0b1101101
# 0b110110100000000
# 0b1100001
# 0b110000100000000
# 0b1100110
# 0b110011000000000
# 0b1100001
# 0b110000100000000