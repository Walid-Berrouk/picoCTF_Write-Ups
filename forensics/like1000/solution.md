# like1000

## Description

> This .tar file got tarred a lot.

## Write-Up

Test here

<img src="./1.png"
     alt="Markdown Monster icon"
     style="
     width: 80%;
     diplay: box;"
/>

With the given `1000.tar` file with, the first thing we might try is to unzip it

```
tar -xf 1000.tar
```

We get another `999.tar` file :

```
└─$ ls
1000.tar  999.tar  filler.txt
```

When we we unzip this last, we get also a `998.tar` file ...

In order to unzip all nested `tar` archives, let's execute the following script :

```
for i in {1000..1}; do tar -xf "$i.tar"; done
```

With this, it will loop on the created archives and extract the new ones each time until we arrive to the last, which contains the `flag.png`


## Flag

picoCTF{l0t5_0f_TAR5}