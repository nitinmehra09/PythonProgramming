'''
7   = n
14  =n*2
21
28
35
42
49
56
63
70






'''






def table(n): 
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")






n =int(input("Enter a number : "))

table(n)
