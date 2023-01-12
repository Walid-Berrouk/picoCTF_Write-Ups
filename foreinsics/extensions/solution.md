# extensions

## Description

> This is a really weird text file TXT? Can you find the flag?

## Hints

> How do operating systems know what kind of file it is? (It's not just the ending!
>
> Make sure to submit the flag as picoCTF{XXXXX}

## Write-Up

As we get the `flag.txt` and from the name of the challenge, it may lead us to check the file extension :

```
file flag.txt
```

```
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```

As we can see, the file isn't actually a plain text file but an image, so let's change its extension to `.png`. We will see the flag displays right away


## Flag

picoCTF{now_you_know_about_extensions}