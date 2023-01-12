# Pixelated

## Write-Up

Hint 2 : Think of different ways you can "stack" images

```
zlib-flate -uncompress < ./29.zlib > uncompressed_1
```

```
zlib-flate -uncompress < ./29.zlib > uncompressed_2
```

```
└─$ file uncompressed_2
uncompressed_2: Tower/XP rel 2 object
```

```
pip install opencv-python
```

## Flag

picoCTF{0542dc1d}

## More information

Write-up : https://ctftime.org/writeup/28930