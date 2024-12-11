def geater(a,b,c):
    if(a<b):
        if(b<c):
            return c
        else:
            return b
    else:
        if (a<c):
            return c
        else:
            return a
        

a =int(input("Enter 1st numbers: "))
b =int(input("Enter 2nd numbers: "))
c =int(input("Enter 3rd numbers: "))

print("The greater number is: ", geater(a, b, c))