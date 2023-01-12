# Trivial Flag Transfer Protocol

## Write-Up

After wornloading the wireshark capture, we open it using wireshark :

`wireshark tftp.pcapng`

we can see when filterin on `tftp` protocol (hint from title of challenge), that it transfered a lot of files since there is a lot of packages, the first one is instructions.txt (sawn in the first packet). So the first thing to do is to reconstitute all the files sent. To do that we go to "File > Export Objects > TFTP ..."

After that, we hit on "Save All" and we choose location.

The next thing is to try to decrypt `plan` and `instructions.txt`, with no result.

After that try to execute the `program.deb` using the following command :

`sudo dpkg -i program.deb`

It gave the following result :

```
(Reading database ... 462876 files and directories currently installed.)
Preparing to unpack program.deb ...
Unpacking steghide (0.5.1-9.1+b1) over (0.5.1-9.1+b1) ...
Setting up steghide (0.5.1-9.1+b1) ...
Processing triggers for man-db (2.11.0-1+b1) ...
Processing triggers for kali-menu (2022.4.1) ...
```

We might think that there is something that, using the program, will be hidden in the pictures using steganography.

After the execution of the program which actually installed `steghide` in our computer. So let's find out what this package do using this command :

`steghide --help`

From here, we can use `steghide` to check for hidden data by extracting from the files gives (pictures). To do that, we use following command :

```
steghide extract -sf FILENAME
```
When trying this command on all given photos (which are more probable to hide data), we can see that is asks for a `passphrase` in order to extract the data. To search for that `passphrase`, we need to check the other extracted files like `plan` file or the `instructions.txt` file.

After openning the files, we can clearly deduce that they are both encrypted. To decrypt them, we use https://www.boxentriq.com/ platform with **Auto Analysis**. Atfer analysis, we find that it is encrypted with `caesar cipher` with key `13`, i.e `ROT13`.

after decrypting each file, we get the following data :

 - For the `instructions.txt` file :

```
tftp doesnt encrypt our traffic so we must disguise our flag transfer figure out away to hide the flag and i will check back for the plan
```

 - For the `plan` file :

```
i used the program and hid it with due diligence check out the photos
```

From those setences, we can suspect that one of its words are the `passphrase` for the pictures. After multiple tries, we find the `DUE DILIGENCE` is the passphrase.

When we pass it to the command line, we receive the following output :

```
└─$ steghide extract -sf ./exported/picture3.bmp
Enter passphrase: 
wrote extracted data to "flag.txt".
```

Clearly, we find a `flag.txt` file extracted with the flag int it.

**Note :** Binwalking, or checking other files like `program.deb` are useless manoeuvres to do


## Flag

picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}

## More Information :

Check the "extracting-files-network-packet-captures_9206.pdf" file for the reconstitution of files from a wireshark capture.

Interesting commands :

 - `binwalk FILENAME` : scan magic bytes (linux property) of a file and see if it occurs be a potential files inside it
 - `binwalk -e FILENAME` : the `-e` extract the file in the found file extensions
 - `tar -xf FILENAME` : extract gzip compressed file
 - `tree DIRECTORU` : is a recursive directory listing command or program that produces a depth-indented listing of files. 
 - `file *` : show informations of all files inside the current directory. the `*` can be replaced with a relative path.
 - `ls -l` or `ll` : give more details of the files (rights, size ...)