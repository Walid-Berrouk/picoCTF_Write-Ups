After connecting to the website, we can see that some data is sent, with different strings, so we start to put those messages in a file :

`nc jupiter.challenges.picoctf.org 14291 > output.txt`

After that, we may suspect that the flag is between those messages, so we make a basic search using `grep` command :

`cat output.txt | grep 'picoCTF{'`

the flag : picoCTF{digital_plumb3r_ea8bfec7}

Note : we could directly use the pip on the netcat connection.

Mote Information : 
http://www.linfo.org/pipes.html