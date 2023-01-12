# First Find

## Write-Up

With the given `.zip` file, we are asked to look for the `uber-secret.txt` file in the extracted folder :

### Solution 1 : Unzip command

After unziping the file, the `unzip` command will show all created files and folders : 

```
unzip files.zip
```

```
Archive:  files.zip
   creating: files/
   creating: files/satisfactory_books/
   creating: files/satisfactory_books/more_books/
  inflating: files/satisfactory_books/more_books/37121.txt.utf-8  
  inflating: files/satisfactory_books/23765.txt.utf-8  
  inflating: files/satisfactory_books/16021.txt.utf-8  
  inflating: files/13771.txt.utf-8   
   creating: files/adequate_books/
   creating: files/adequate_books/more_books/
   creating: files/adequate_books/more_books/.secret/
   creating: files/adequate_books/more_books/.secret/deeper_secrets/
   creating: files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/
 extracting: files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt  
  inflating: files/adequate_books/more_books/1023.txt.utf-8  
  inflating: files/adequate_books/46804-0.txt  
  inflating: files/adequate_books/44578.txt.utf-8  
   creating: files/acceptable_books/
   creating: files/acceptable_books/more_books/
  inflating: files/acceptable_books/more_books/40723.txt.utf-8  
  inflating: files/acceptable_books/17880.txt.utf-8  
  inflating: files/acceptable_books/17879.txt.utf-8  
  inflating: files/14789.txt.utf-8   
```

### Solution 2 : tree command

The `tree` command is a command that will give you a tree of folders and files recursivly throughout the specified folder.

**Note :** Note that th `-a` option is important to show hidden folders and files :

```
tree -a ./files
```

```
./files
├── 13771.txt.utf-8
├── 14789.txt.utf-8
├── acceptable_books
│   ├── 17879.txt.utf-8
│   ├── 17880.txt.utf-8
│   └── more_books
│       └── 40723.txt.utf-8
├── adequate_books
│   ├── 44578.txt.utf-8
│   ├── 46804-0.txt
│   └── more_books
│       ├── 1023.txt.utf-8
│       └── .secret
│           └── deeper_secrets
│               └── deepest_secrets
│                   └── uber-secret.txt
└── satisfactory_books
    ├── 16021.txt.utf-8
    ├── 23765.txt.utf-8
    └── more_books
        └── 37121.txt.utf-8

9 directories, 12 files
```

What you have to do is to write the path to the file and print it content.

### Solution 3 : find command

Which is the entended solution, it is the use of `find` command which helps you find a file using its name or a part of it, and give you back the path to it :

```
find ./files -name "uber-secret.txt"
```

```
./files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

Now We need to only read the file :

```
cat files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

```
picoCTF{f1nd_15_f457_ab443fd1}
```

## Flag

picoCTF{f1nd_15_f457_ab443fd1}
