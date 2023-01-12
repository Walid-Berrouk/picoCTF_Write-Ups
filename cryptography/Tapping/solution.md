# Tapping

## Description

> Theres tapping coming in from the wires. What's it saying `nc jupiter.challenges.picoctf.org 9422`.

## Hints

> What kind of encoding uses dashes and dots?
>
> The flag is in the format PICOCTF{}

## Write-Up

After connecting to the instance, we receive directly a morse sequence :

```
nc jupiter.challenges.picoctf.org 9422
```

```
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- -.... ---.. ...-- ---.. ..--- ....- -.... .---- ----- } 
```

So, using an online tool like [this website](https://morsedecoder.com/fr/), we can easily decode it :

```
PICOCTF#M0RS3C0D31SFUN2683824610#
```


## Flag

PICOCTF{M0RS3C0D31SFUN2683824610}