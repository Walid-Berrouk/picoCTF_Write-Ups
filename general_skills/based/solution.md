# Based

## Write-Up

This challenge is aimed to challenge your conversion skills, it can be solved using :

 - **Scripting :** Using pwn tools
 - **Python Interactive Conversion:** by using python interractive and convert each word
 - **Cyberchef :** By using an online tool look cuberchef, and use `magic` conversion to check for conversion type and convert it on the go.

When connecting to the challenge at `nc jupiter.challenges.picoctf.org 15130`, it will interractivaly give you words to convert. The based used are :

 - Binary
 - Octal
 - Hex

After using cyberchef, here is what a communication look like :

```
└─$ nc jupiter.challenges.picoctf.org 15130
Let us see how data is stored
falcon
Please give the 01100110 01100001 01101100 01100011 01101111 01101110 as a word.
...
you have 45 seconds.....

Input:
falcon
Please give me the  146 141 154 143 157 156 as a word.
Input:
falcon
Please give me the 736c75646765 as a word.
Input:
sludge
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_02167de8}
```

## Flag

picoCTF{learning_about_converting_values_02167de8}

## More information

Cyberchef : https://gchq.github.io/CyberChef/