import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
# print(ALPHABET)

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
		# print(c, ord(c), binary, int(binary[:4]), int(binary[:4], 2), int(binary[4:]), int(binary[4:], 2))
	return enc

def b16_decode(enc):
	plain = ""
	cpt = 0

	# Convert from int x to binary with a n bits length
	getbinary = lambda x, n: format(x, 'b').zfill(n)

	# letter bits
	letter_binary=""
	for c in enc:
		if cpt == 0 :
			letter_binary = str(getbinary(ALPHABET.index(c), 4))
			cpt = 1
		else :
			letter_binary += str(getbinary(ALPHABET.index(c), 4))
			plain += chr(int(letter_binary, 2))
			cpt = 0
	return plain

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def reshift(c, k):
	t3 = ALPHABET.index(c)

	# we know that
	# t3 == (t1 + t2) % len(ALPHABET)
	# we can have either
	# (t1 + t2) == t3
	# (t1 + t2)  == len(ALPHABET) + t3
	# this one is valid if the first one is negative
	# (t1 + t2) == len(ALPHABET)*2 + t3
	# this one is neglected seeing the prints result
	# (t1 + t2) == len(ALPHABET)*3 + t3

	# print(t3 - t2, end =" ")
	# print(len(ALPHABET) + t3 - t2 , end =" ")
	# print(len(ALPHABET)*2 + t3 - t2, end =" ")
	# print(len(ALPHABET)*3 + t3 - t2)


	# t2 = ord(k) - LOWERCASE_OFFSET

	# c2 = len(ALPHABET) + t3 - t2
	# if (t3 - t2) >= 0 :
	# 	c1 = t3 - t2
	# else :
	# 	c1 = len(ALPHABET)*2 + t3 - t2

	# return chr(c1 + LOWERCASE_OFFSET), chr(c2 + LOWERCASE_OFFSET)

	# Actually it takes the one which is under 16

	t2 = ord(k) - LOWERCASE_OFFSET

	c2 = len(ALPHABET) + t3 - t2
	if (t3 - t2) >= 0 :
		c1 = t3 - t2
	else :
		c1 = len(ALPHABET)*2 + t3 - t2

	if (c1) < 16 :
		return chr(c1 + LOWERCASE_OFFSET)
	else :
		return chr(c2 + LOWERCASE_OFFSET)

flag = "redacted"
key = "redacted"
# assert all([k in ALPHABET for k in key])
# assert len(key) == 1

print(flag)
b16 = b16_encode(flag)
print(b16)
b16_dec = b16_decode(b16)
print(b16_dec)


enc = ""
for i, c in enumerate(b16):
	# print(i,c)
	# print(ord("z") - LOWERCASE_OFFSET, len(ALPHABET))
	enc += shift(c, key[i % len(key)])
print(enc)

# pool_plain= []
# for i, c in enumerate(enc):

# 	possibilities_tuple = reshift(c, key[i % len(key)])
# 	if pool_plain == [] :
		
# 		if b16[i] == possibilities_tuple[0]: print("1", b16[i], c, possibilities_tuple[0],possibilities_tuple[1])
# 		else : print("2", b16[i], c, possibilities_tuple[0],possibilities_tuple[1])
# 		for k in possibilities_tuple :
# 			pool_plain.append(k)
# 	else :
# 		# print(possibilities_tuple)
# 		if b16[i] == possibilities_tuple[0]: print("1", b16[i], c, possibilities_tuple[0],possibilities_tuple[1])
# 		else : print("2", b16[i], c, possibilities_tuple[0],possibilities_tuple[1])
		# tmp = []
		# for j in pool_plain :
		# 	for k in possibilities_tuple :
		# 		tmp.append(j+k)
		# for l in tmp :
		# 	pool_plain.append(l)

# pool_plain_final = []
# for c in pool_plain:
# 	if len(c) == len(enc): pool_plain_final.append(c)


# print(pool_plain_final)

plain = ""
for i, c in enumerate(enc):

	plain += reshift(c, key[i % len(key)])

print(plain)
