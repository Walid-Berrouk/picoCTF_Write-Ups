# vault-door-3

## Description

> This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](VaultDoor3.java)

## Hints

> 

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

What the `checkPassword()` do is actually scrumbling the flag, then compare it to a certain string :

```java
...
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
    }
...
```

Let's reverse the logic used:

```py
In [1]: len("jU5t_a_sna_3lpm18g947_u_4_m9r54f")
Out[1]: 32

In [2]: str = "jU5t_a_sna_3lpm18g947_u_4_m9r54f"

# This part will remain as is
In [3]: str[:8]
Out[3]: 'jU5t_a_s'

# This part will be merroed on itself
In [4]: str[8:16]
Out[4]: 'na_3lpm1'

# This part is mixted with it self
In [5]: str[16:32]
Out[5]: '8g947_u_4_m9r54f'

# Here are the indexes generated from the loops
In [9]: for i in range(31, 16, -2):
   ...:     print(i, end=" ")
   ...: 
31 29 27 25 23 21 19 17 
In [10]: for i in range(16, 32, 2):
    ...:     print(i, end=" ")
    ...: 
16 18 20 22 24 26 28 30 
In [11]: for i in range(8, 16, 1):
    ...:     print(23 - i, end=" ")
    ...: 
15 14 13 12 11 10 9 8 
In [12]: for i in range(16, 32, 2):
    ...:     print(46 - i, end=" ")
    ...: 
30 28 26 24 22 20 18 16 
In [13]: for i in range(0, 8, 1):
    ...:     print(i, end=" ")
    ...: 
0 1 2 3 4 5 6 7 


# This is our reverse program
In [15]: sorting = []

In [16]: for i in range(0, 8, 1):
    ...:     sorting.append(( i,i ))
    ...: 

In [17]: sorting
Out[17]: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]

In [18]: for i in range(8, 16, 1):
    ...:     sorting.append(( i, 23 - i ))
    ...: 

In [19]: for i in range(16, 32, 2):
    ...:     sorting.append(( i, 46 - i ))
    ...: 

In [20]: for i in range(31, 16, -2):
    ...:     sorting.append(( i,i ))
    ...: 

In [21]: sorting
Out[21]: 
[(0, 0),
 (1, 1),
 (2, 2),
 (3, 3),
 (4, 4),
 (5, 5),
 (6, 6),
 (7, 7),
 (8, 15),
 (9, 14),
 (10, 13),
 (11, 12),
 (12, 11),
 (13, 10),
 (14, 9),
 (15, 8),
 (16, 30),
 (18, 28),
 (20, 26),
 (22, 24),
 (24, 22),
 (26, 20),
 (28, 18),
 (30, 16),
 (31, 31),
 (29, 29),
 (27, 27),
 (25, 25),
 (23, 23),
 (21, 21),
 (19, 19),
 (17, 17)]

In [22]: sorted(sorting)
Out[22]: 
[(0, 0),
 (1, 1),
 (2, 2),
 (3, 3),
 (4, 4),
 (5, 5),
 (6, 6),
 (7, 7),
 (8, 15),
 (9, 14),
 (10, 13),
 (11, 12),
 (12, 11),
 (13, 10),
 (14, 9),
 (15, 8),
 (16, 30),
 (17, 17),
 (18, 28),
 (19, 19),
 (20, 26),
 (21, 21),
 (22, 24),
 (23, 23),
 (24, 22),
 (25, 25),
 (26, 20),
 (27, 27),
 (28, 18),
 (29, 29),
 (30, 16),
 (31, 31)]

In [25]: for i in sorted(sorting) :
    ...:     print(str[i[1]], end="")
    ...: 
jU5t_a_s1mpl3_an4gr4m_4_u_79958f
```

**Note** : you can reverse the logic with Javascript since the syntax is similar using node.

## Flag

picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}

## More Information

 - **Anagrams :** Anagrams are words or phrases you spell by rearranging the letters of another word or phrase. 