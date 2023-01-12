# Easy Peasy

## Write-Up

### Introduction

From the service implementation, we see that it uses a XOR pad of length 50000 to encrypt the input. This should be unbreakable if it's used as a one-time-pad, but in our case the service performs a wrap-around and reuses the same pad for every 50000 characters.

So, to retrieve the XOR values used to encrypt the flag, we just need to cause a wraparound, allowing our known input to be re-encrypted with the same XOR values. Since we know the input, we can XOR it with the encrypted result to get the key. Then, it's just a matter of XOR-ing the key with the encrypted flag.

In fact, we can even make this a bit more efficient by re-encrypting the same encrypted flag with the XOR stream that was used to originally encrypt it. This should result in the plaintext flag.

### Explanation

First of all, we can see that the applied operation is the xor :

```python
ciphertext = flag ^ key[0:len(flag)]
```

And we notice that even if the key length is too big (50000), it will use it back when we encrupted all 50000 characters :

```python
...
stop = key_location + len(ui)

...

if stop >= KEY_LEN:
    stop = stop % KEY_LEN
...
```

So, the one-tap is after all a xor with parts of a big key. But in fact, and with the properties of the xor, if we give it enough characters to make a cycle or a wraparround on the key (get the `start` variable back to 0) then send the encrypted flag, it will give us the decrypted flag.

Before hop into the exploit, let's check a little bit more the code and outputs :

 - We can see that for each character of the flag, it resturns two characters : 

```
└─$ /usr/bin/python3 -u "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py"                                                                                         130 ⨯
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
45

What data would you like to encrypt? ^CTraceback (most recent call last):
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 51, in <module>
    c = encrypt(c)
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 25, in encrypt
    ui = input("What data would you like to encrypt? ").rstrip()
KeyboardInterrupt


┌──(rivench㉿kali)-[~/Documents/picoCTF/cryptography/Easy_Peasy]
└─$ /usr/bin/python3 -u "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py"                                                                                         130 ⨯
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
4544

What data would you like to encrypt? ^CTraceback (most recent call last):
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 51, in <module>
    c = encrypt(c)
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 25, in encrypt
    ui = input("What data would you like to encrypt? ").rstrip()
KeyboardInterrupt


┌──(rivench㉿kali)-[~/Documents/picoCTF/cryptography/Easy_Peasy]
└─$ /usr/bin/python3 -u "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py"                                                                                         130 ⨯
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
454445

What data would you like to encrypt? ^CTraceback (most recent call last):
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 51, in <module>
    c = encrypt(c)
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 25, in encrypt
    ui = input("What data would you like to encrypt? ").rstrip()
KeyboardInterrupt


┌──(rivench㉿kali)-[~/Documents/picoCTF/cryptography/Easy_Peasy]
└─$ /usr/bin/python3 -u "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py"                                                                                         130 ⨯
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
45444544

What data would you like to encrypt? ^CTraceback (most recent call last):
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 51, in <module>
    c = encrypt(c)
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 25, in encrypt
    ui = input("What data would you like to encrypt? ").rstrip()
KeyboardInterrupt


┌──(rivench㉿kali)-[~/Documents/picoCTF/cryptography/Easy_Peasy]
└─$ /usr/bin/python3 -u "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py"                                                                                         130 ⨯
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
454445444c

What data would you like to encrypt? ^CTraceback (most recent call last):
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 51, in <module>
    c = encrypt(c)
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 25, in encrypt
    ui = input("What data would you like to encrypt? ").rstrip()
KeyboardInterrupt


┌──(rivench㉿kali)-[~/Documents/picoCTF/cryptography/Easy_Peasy]
└─$ /usr/bin/python3 -u "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py"                                                                                         130 ⨯
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
455d565b7530771f49055d59576758126a5b50535356505847484d

What data would you like to encrypt? ^CTraceback (most recent call last):
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 51, in <module>
    c = encrypt(c)
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 25, in encrypt
    ui = input("What data would you like to encrypt? ").rstrip()
KeyboardInterrupt


┌──(rivench㉿kali)-[~/Documents/picoCTF/cryptography/Easy_Peasy]
└─$ /usr/bin/python3 -u "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py"                                                                                         130 ⨯
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
455d565b7530771f49055d59576758126a5b50535356505847484d

What data would you like to encrypt? ^CTraceback (most recent call last):
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 51, in <module>
    c = encrypt(c)
  File "/home/rivench/Documents/picoCTF/cryptography/Easy_Peasy/otp.py", line 25, in encrypt
    ui = input("What data would you like to encrypt? ").rstrip()
KeyboardInterrupt
```

```
└─$ python3                                                                                                                                                                      130 ⨯
Python 3.10.8 (main, Oct 24 2022, 10:07:16) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> len('455d565b7530771f49055d59576758126a5b50535356505847484d')
54
>>> len('picoCTF{yahia_is_legendary}')
27
>>> exit
```

This caracteristic comes fromof the `hexlify` function that is applied to the output. So we need to watch out on the length when sending payloads. And we have :

```
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b

What data would you like to encrypt? 
```

So, The length of the flag is 32, since the encrypted string givend is 64. But it isn't a matter of lenfth only but also a value. So, we need to unhexlify the output each time using `unhex` of `binascii`, this way, we get the original value and length

 - Here is the script we used : 

```python
#! /usr/bin/python3

from pwn import *
from binascii import unhexlify

HOST = 'mercury.picoctf.net'
PORT = 20266

p = remote(HOST, PORT)

# First prints
p.recvline()
p.recvline()
encrypted_flag = p.recvline().strip()
bin_encrypted_flag =  unhexlify(encrypted_flag)

exploit = "a"*(50000 - len(bin_encrypted_flag))

p.sendlineafter(b'What data would you like to encrypt? ', exploit.encode())
p.sendlineafter(b'What data would you like to encrypt? ', bin_encrypted_flag)
p.recvline()
print("The Flag is : " + unhex(p.recvline().strip()).decode())
p.interactive()
```

 - After Executing script :

```
[+] Opening connection to mercury.picoctf.net on port 20266: Done
The Flag is : 99072996e6f7d397f6ea0128b4517c23
[*] Switching to interactive mode
```


## Flag

picoCTF{99072996e6f7d397f6ea0128b4517c23}

## More Information

- https://en.wikipedia.org/wiki/One-time_pad
- http://www.crypto-it.net/eng/attacks/two-time-pad.html
- https://crypto.stackexchange.com/questions/2249/how-does-one-attack-a-two-time-pad-i-e-one-time-pad-with-key-reuse
- WriteUp : https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Easy_Peasy.md