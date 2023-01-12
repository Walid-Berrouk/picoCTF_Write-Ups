# vault-door-1

## Description

> This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: VaultDoor1.java

## Hints

> Look up the charAt() method online.

## Write-Up

After checking the `java` file, we can find that it has a password checker method called `checkPassword` that checks each character from our input with another one.

```java
...
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e';
    }
...
```

In order to recover the flag, all we have to do is to place each character in the right position as its `password.charAt()` method is saying.


```py
In [1]: flag = '''
   ...:                password.charAt(0)  == 'd' &&
   ...:                password.charAt(29) == '9' &&
   ...:                password.charAt(4)  == 'r' &&
   ...:                password.charAt(2)  == '5' &&
   ...:                password.charAt(23) == 'r' &&
   ...:                password.charAt(3)  == 'c' &&
   ...:                password.charAt(17) == '4' &&
   ...:                password.charAt(1)  == '3' &&
   ...:                password.charAt(7)  == 'b' &&
   ...:                password.charAt(10) == '_' &&
   ...:                password.charAt(5)  == '4' &&
   ...:                password.charAt(9)  == '3' &&
   ...:                password.charAt(11) == 't' &&
   ...:                password.charAt(15) == 'c' &&
   ...:                password.charAt(8)  == 'l' &&
   ...:                password.charAt(12) == 'H' &&
   ...:                password.charAt(20) == 'c' &&
   ...:                password.charAt(14) == '_' &&
   ...:                password.charAt(6)  == 'm' &&
   ...:                password.charAt(24) == '5' &&
   ...:                password.charAt(18) == 'r' &&
   ...:                password.charAt(13) == '3' &&
   ...:                password.charAt(19) == '4' &&
   ...:                password.charAt(21) == 'T' &&
   ...:                password.charAt(16) == 'H' &&
   ...:                password.charAt(27) == '5' &&
   ...:                password.charAt(30) == '2' &&
   ...:                password.charAt(25) == '_' &&
   ...:                password.charAt(22) == '3' &&
   ...:                password.charAt(28) == '0' &&
   ...:                password.charAt(26) == '7' &&
   ...:                password.charAt(31) == 'e';
   ...: '''

In [39]: flag = flag.replace('password.charAt(', '')

In [40]: print(flag)

               0)  == 'd' &&
               29) == '9' &&
               4)  == 'r' &&
               2)  == '5' &&
               23) == 'r' &&
               3)  == 'c' &&
               17) == '4' &&
               1)  == '3' &&
               7)  == 'b' &&
               10) == '_' &&
               5)  == '4' &&
               9)  == '3' &&
               11) == 't' &&
               15) == 'c' &&
               8)  == 'l' &&
               12) == 'H' &&
               20) == 'c' &&
               14) == '_' &&
               6)  == 'm' &&
               24) == '5' &&
               18) == 'r' &&
               13) == '3' &&
               19) == '4' &&
               21) == 'T' &&
               16) == 'H' &&
               27) == '5' &&
               30) == '2' &&
               25) == '_' &&
               22) == '3' &&
               28) == '0' &&
               26) == '7' &&
               31) == 'e';


In [41]: flag = flag.replace(' ', '')

In [42]: print(flag)

0)=='d'&&
29)=='9'&&
4)=='r'&&
2)=='5'&&
23)=='r'&&
3)=='c'&&
17)=='4'&&
1)=='3'&&
7)=='b'&&
10)=='_'&&
5)=='4'&&
9)=='3'&&
11)=='t'&&
15)=='c'&&
8)=='l'&&
12)=='H'&&
20)=='c'&&
14)=='_'&&
6)=='m'&&
24)=='5'&&
18)=='r'&&
13)=='3'&&
19)=='4'&&
21)=='T'&&
16)=='H'&&
27)=='5'&&
30)=='2'&&
25)=='_'&&
22)=='3'&&
28)=='0'&&
26)=='7'&&
31)=='e';


In [43]: flag = flag.replace(')', '')

In [44]: flag = flag.replace('&&', '')

In [45]: flag = flag.replace("'", '')

In [47]: flag = flag.replace(";", '')

In [48]: print(flag)

0==d
29==9
4==r
2==5
23==r
3==c
17==4
1==3
7==b
10==_
5==4
9==3
11==t
15==c
8==l
12==H
20==c
14==_
6==m
24==5
18==r
13==3
19==4
21==T
16==H
27==5
30==2
25==_
22==3
28==0
26==7
31==e

In [50]: flag.split("\n")
Out[50]: 
['',
 '0==d',
 '29==9',
 '4==r',
 '2==5',
 '23==r',
 '3==c',
 '17==4',
 '1==3',
 '7==b',
 '10==_',
 '5==4',
 '9==3',
 '11==t',
 '15==c',
 '8==l',
 '12==H',
 '20==c',
 '14==_',
 '6==m',
 '24==5',
 '18==r',
 '13==3',
 '19==4',
 '21==T',
 '16==H',
 '27==5',
 '30==2',
 '25==_',
 '22==3',
 '28==0',
 '26==7',
 '31==e',
 '']

In [51]: flag = flag.split("\n")

In [53]: flag_dic = {}

In [54]: for c in flag :
    ...:     if len(c) > 1 :
    ...:         ch = c.split("==")
    ...:         flag_dic[int(ch[0])] = ch[1]
    ...: 

In [55]: print(flag_dic)
{0: 'd', 29: '9', 4: 'r', 2: '5', 23: 'r', 3: 'c', 17: '4', 1: '3', 7: 'b', 10: '_', 5: '4', 9: '3', 11: 't', 15: 'c', 8: 'l', 12: 'H', 20: 'c', 14: '_', 6: 'm', 24: '5', 18: 'r', 13: '3', 19: '4', 21: 'T', 16: 'H', 27: '5', 30: '2', 25: '_', 22: '3', 28: '0', 26: '7', 31: 'e'}


In [52]: flag_rec = ""

In [56]: for i in range(32):
    ...:     flag_rec += flag_dic[i]
    ...: 

In [57]: print(flag_rec)
d35cr4mbl3_tH3_cH4r4cT3r5_75092e
```

Finally, let's wrap it in `picoCTF{}` format.


## Flag

picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}