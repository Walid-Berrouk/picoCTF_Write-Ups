here is the given encrypted flag : cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

and we know that it is encrypted using ROT13, which is ROT13 ("rotate by 13 places", sometimes hyphenated ROT-13) is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the alphabet. ROT13 is a special case of the Caesar cipher which was developed in ancient Rome. 

and we know that the flag is wrapped into picoCTF{}, so :
c -> p
v -> i
p -> c
b -> o
g -> t
s -> f

but before continuing more, we can use the `script.py` that is a particular case of ceasor but with rotation number (i) of 13

flag : picoCTF{not_too_bad_of_a_problem}