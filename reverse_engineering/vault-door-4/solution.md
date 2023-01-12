# vault-door-4

## Description

> This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](VaultDoor4.java)


## Hints

> Use a search engine to find an "ASCII table"
>
> You will also need to know the difference between octal, decimal, and hexadecimal numbers.

## Write-Up

When we check the given `java` code, we can see that our flag is first being stripped from its format, then passed to a `checkPassword()` method :

```java
...
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
...
```

What the `checkPassword()` do is actually comparing each char or byte of our input with another byte, but each one with a different base or encoding :


```java
...
public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146,
            '4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
...
```

Note also the remark left in the code :

```java
    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
```

And from the hints, we can deduce that first row of the bytes is actually `ASCII` bytes :

```java
...
106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
...
```

The other ones are `hex` :

```java
...
0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
...
```

Others are `octal` :

```java
...
0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146,
...
```

> JavaScript you can use octals and hexadecimals.
>
> The following are examples of **octal** numbers:
> 
> 01234 -077 0312
> 
> Positive octal numbers must begin with `0` (zero) followed by octal digit(s).
> 
> Negative octal numbers must begin with -0 followed by octal digit(s).
>
> And these are examples of **hexadecimal** numbers:
> 
> 0xFF -0xCCFF 0xabcdef
> 
> Positive hexadecimals must begin with `0x` and negative hexadecimals must begin with -0x. 

**Note :**

```js
>> console.log(String.fromCharCode(0142))
> 'b' 


>> 0142
> 98
```


And last ones are just `chars` :

```java
...
'4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ,
...
```

So Let's try to recover the flag by decode that array of bytes (note the change of octal representation in python) :


```py
In [1]: flag = [
   ...:             106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
   ...:             0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
   ...:             0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o70 , 0o146,
   ...:             '4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ,
   ...:         ]

In [2]: for i in flag:
   ...:     if type(i) == str:
   ...:         print(i, end="")
   ...:     else :
   ...:         print( chr(i), end="")
   ...: 
jU5t_4_bUnCh_0f_bYt3s_8f4a6cbf3b
```

Another solution is to use javascript to convert all elements back :

```js
>> console.log(String.fromCharCode(106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  , 0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f, 0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146) + [ '4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ].join(""))

> 'jU5t_4_bUnCh_0f_bYt3s_8f4a6cbf3b'
```

## Flag

picoCTF{jU5t_4_bUnCh_0f_bYt3s_8f4a6cbf3b}

## More Information

 - Octal and hex representation in javascript :
   - https://stackoverflow.com/questions/37003770/why-javascript-treats-a-number-as-octal-if-it-has-a-leading-zero
   - http://www.javascripter.net/faq/octalsan.htm
 - Octal and hex representation in python :
   - https://towardsdatascience.com/binary-hex-and-octal-in-python-20222488cee1
