# Dachshund Attack

## Write-Up

After targetting the problem, here what you get  :

```
┌──(rivench㉿kali)-[~/Documents/picoCTF/Dachshund_Attack]
└─$ nc mercury.picoctf.net 31133
Welcome to my RSA challenge!
e: 34292914393228338914166643090771061804173787077768092181105401327140711058208996268912025744896935208863358246234337512005906443391185529217719947522831797313602572497150343095922785499731192546570277475491542485418251051634587496112162305225681486846004607198528011365540735525567381322268668178904912740599
n: 81827622374443127655427402634327309651949614487969061562166927933112499530352122984282678174592294675517014748858677205531043813187828524155941840328145265678178532758543864064520625372065208359261344797760599741760646252331891727652133273913410676070982781513131940744875255442711385568235258258178956602619
c: 51025631385794160707543390177364556850233454202348462887253047241772652786098116976984288637439792983366978742705044847503893723705942097483301631777641870307718997264244408360058187831391603480032525907638044025177020915463013321465004720104938037981417926855341549563278945442849228559108774867373733885960

```

It is obviously params for RSA encryption : exponent, n and cipher

Since the exponent is too big, we can decrypt it using weak numbers attack of n and e

but in the decription we have the following hint : `What if d is too small?`, we conclude that a brute force on d may work (check `decrypt.py` for the code of decryption (you can use a pre-defined library like `rsa` (remember to install rsa using `pip install rsa`)))

But after multiple tests, we conclude that this is note the way.

After more investigation on small `d` values attack, we find the `weiner attack`, an attack based on the `weiner theorem` which help hus guess the `d` value when it is used small (check More Information Section for more details)

For the implimentation, we used the `owiener` library to performe the attack (remember to install the library using `python3 -m pip install owiener`), here is the script : 

```python
#! /usr/bin/python3

from Crypto.Util.number import *
import owiener

f = open('output.txt', 'r')
e = int(f.readline().split(":")[1])
n = int(f.readline().split(":")[1])
c = int(f.readline().split(":")[1].strip())

# Decryption with weiner Attack
d = owiener.attack(e, n)

if d is None:
    print("Failed")
else:
    print("Hacked d={}".format(d))
    flag = long_to_bytes(pow(c, d, n))
    print(f"Decrypted flag : {flag}")
```


Here is the script after execution :

```
└─$  /usr/bin/python3 "/home/rivench/Documents/picoCTF/cryptography/Dachshund_Attack/decrypt.py"
Hacked d=16779708078312244376844016863157743386017830379368167121706344896542005473119
Decrypted flag : b'picoCTF{proving_wiener_1146084}'
```

## Flag

picoCTF{proving_wiener_1146084}

## More Information 
https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/

weak numbers attack : 
 - https://stackoverflow.com/questions/49878381/rsa-decryption-using-only-n-e-and-c
 - https://github.com/RsaCtfTool/RsaCtfTool

Weiner Attack (RSA Attack on small d values):
 - Description : https://en.wikipedia.org/wiki/Wiener%27s_attack
 - Explanation (With Code) : https://sagi.io/crypto-classics-wieners-rsa-attack/
 - Implimentation : https://github.com/orisano/owiener

Write-Up : https://ctf.zeyu2001.com/2021/picoctf/dachshund-attacks-80