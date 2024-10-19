n = int(input("Enter the number : "))
i=n
f=1
while n!=0 :
    f *= n
    n -= 1

print("Factorial of", i, "is", f)