import string

LOWERCASE_OFFSET = ord("a")
limit=16
ALPHABET = string.ascii_lowercase[:limit]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
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

def unshift(c, k):
	t3 = ALPHABET.index(c)

	# it takes the one which is under 16

	t2 = ord(k) - LOWERCASE_OFFSET

	# c2 = len(ALPHABET) + t3 - t2
	# if (t3 - t2) >= 0 :
	# 	c1 = t3 - t2
	# else :
	# 	c1 = len(ALPHABET)*2 + t3 - t2

	# if (c1) < limit :
	# 	return chr(c1 + LOWERCASE_OFFSET)
	# else :
	# 	return chr(c2 + LOWERCASE_OFFSET)


	return chr(((len(ALPHABET) + t3 - t2) % limit) + LOWERCASE_OFFSET)

# The assert statements show that the key needs to be one character and be a letter between a to p. It is necessary to change the values of flag and key in order to get an output of "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"

# assert all([k in ALPHABET for k in key])
# assert len(key) == 1

# Test the cycle of encrypt-Decrypt

# flag = "redacted"
# key = "redacted"

# print(flag)
# b16 = b16_encode(flag)
# print(b16)

# enc = ""
# for i, c in enumerate(b16):
# 	enc += shift(c, key[i % len(key)])
# print(enc)

# plain = ""
# for i, c in enumerate(enc):
# 	plain += unshift(c, key[i % len(key)])
# print(plain)

# b16_dec = b16_decode(plain)
# print(b16_dec)


# Decrypt the flag 
print()

for key in ALPHABET : 
	flag_enc = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"

	plain = ""
	for i, c in enumerate(flag_enc):
		plain += unshift(c, key[i % len(key)])
	print(plain)

	b16_dec = b16_decode(plain)
	print(b16_dec)