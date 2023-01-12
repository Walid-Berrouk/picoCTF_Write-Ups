# Big Zip

## Write-Up

After downloading and unziping the `.zip` given file, it will generate a tone of files and subfolders that we might suspect the flag to be in one of those files, but we can't check them manually.

To execute a recursive search on all files and subfolders files, we use the `grep` command :

```
grep -rni "picoCTF{" *
```

where : 

 - ```r``` = recursive i.e, search subdirectories within the current directory
 - ```n``` = to print the line numbers to stdout
 - ```i``` = case insensitive search


After execution, we get :

```
folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:1:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```

## Flag

flag : picoCTF{gr3p_15_m4g1c_ef8790dc}

## More infromation

https://stackoverflow.com/questions/15286947/how-to-perform-grep-operation-on-all-files-in-a-directory