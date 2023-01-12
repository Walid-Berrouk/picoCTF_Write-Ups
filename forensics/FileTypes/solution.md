# Flag Types

## Write-up

When receiving the `Flag.pdf` file and print its content, we can see clearling that it is a shell archive, so all we have to do is give it the proper execution rights and run it (note that i made a copy and named it `script_sh`):

```
└─$ chmod +x script_sh

└─$ ./script_sh
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
```

**Note :** Note that it needs uudecode in order to run, to install it, run :

```
sudo apt-get install sharutils
```

After running the script, you will get a flag file. when cheking the extension you get :

```
└─$ file flag
flag: current ar archive
```

This is an `ar archive` file, so we need to extract it using `ar` command. First, you can check the members (files) in the archive using the following command :

```
ar p flag
```

and to extract it, we use the following command :

```
└─$ ar xv flag
x - flag
```

Doing this will get us another archive file but this time a `cpio archive` : 

```
└─$ file flag
flag: cpio archive
```

So the obvious thing to do is extract it using `cpio` command. After doing it, we will get another file with another extension etc., so, we need to continue to extract until arriving to the file flag.

Here is the history of commands i run depending on the extensions (Note that some commands need to be installed) :

```
 2232  cpio -h
 2233  cpio --help
 2234  cpio -i flag
 2237  cpio -i < flag
 2241  mkdir cpio_extract
 2242  cd cpio_extract/
 2244  cpio -i < ../flag
 2255  tar -xf flag
 2257  bzip2 --help
 2258  bzip2 -d flag
 2262  gzip --help
 2263  gzip -d flag.out
 2266  mv flag.out flag.gz
 2268  gzip -d flag.gz
 2269  l
 2272  sudo apt-get install lzip
 2273  lzip -h
 2276  cat flag.output
 2277  cat flag.out
 2280  sudo apt-get install lz4
 2281  lz4 -d flag.out
 2282  mv flag.out flag.lz4
 2283  lz4 -d flag.lz4
 2286  file flaf
 2288  lzma -d flag
 2292  cp flag flag.lzma
 2294  la
 2297  rm flag
 2299  lzma -d flag.lzma
 2303  sudo apt-get install lzop
 2304  lzop -d flag
 2305  mv flag flag.lzop
 2306  lzop -d flag.lzop
 2309  lzip -d flag
 2311  file flag.out
 2312  xz -d flag.out
 2313  mv flag.out flag.xz
 2314  xz -d flag.xz
```

At last we need a flag file that it is a `ASCII Text` containning the following hex string :

```
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f39353063346665657d0a
```

After decoding it using a online tool like cyberchef, we get the flag.

## Flag

picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_950c4fee}