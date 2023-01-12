# Buffer Overflow 0

## Write-Up

### Introduction

Whe analysing the code, you can find the following functions use : 

 - `fflush(stdout)` : flush a stream. For output streams, fflush() forces a write of all user-space buffered data for the given output or update stream via the stream's underlying write function.

This functions helps when data is in the buffers program to flush it to output streams like terminal. This is useful when using `netcat` and will block until an interaction happens from the user, it will directly flush out buffers data without that interaction or making user wait indifinatly.

 - `gets()` : get a string from standard input (DEPRECATED).

We can find in the BUGS section that it is deprecated and not used, since it is impossible to tell without knowing the data in advance how many characters gets() will read, and because gets() will continue to store characters past the end of the buffer, it is extremely dangerous to use.  It has been used to break computer security.  Use fgets() instead.

 - `vuln()` : a vulnerable function that, in normal processing, copies a string into a nother using `strcpy` function


In order to get the flag, you can cause a buffer overflow by entering a big amount of characters to overwrite pointers program.

### Tools used

 - `gdb`
 - `gef` : pritifying of `gdb`, see : https://github.com/hugsy/gef 

### Explanation of the attack :

When seeing the code, we can clearly see that it handles the signal of sigmentation fault (SIGSEV) and handles it with a function that prints the flag, so our aim is to cause a **segmentation fault**.

To do that we can try to access a part of the memory that we dont have the right to like pointers of the stack ..., and we can use gets and its vulnerability to do that.

As we can see in `gets` bugs, this function was used to read data indifinatly, so it can read data even longer than the buffers and variables itself. Followed by `strcopy`, which also copies the data from a buffer to another, not depending on the a size, it stops when it finds null byte (delemitor). Meaning that it can copy exactly the content of the first string, not matter how long it is, if it doesn't contain a delimitor in the middle, into the second one without verifying length of the tagettetd one.

In our code, we find that using `gets`, we read data from input, and if we give it enough characters, this data will be read and copied to a buffer of a length 16. Since the data is long enough, it will overwrite important variables like : **saved instruction pointer** from main (since it called the function `vuln` to copy the input data in the buffer). For instance, when the program returns in the main function, it returns to 'aaaa' which is not a valid address which will cause a **segmentation fault**. Other causes of that can be address that we don't have right to access to.

We can use tools like `gdb` or `gef` to check what happens when an error occurs.

**Note :** in order to run `vuln` binary, add execution permissions to it.

## Flag

flag : picoCTF{ov3rfl0ws_ar3nt_that_bad_8ba275ff}