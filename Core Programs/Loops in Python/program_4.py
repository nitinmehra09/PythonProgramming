n = int(input("Enter the random number :"))

for i in range(2,n):
    if(n%i==0):
        print("Number is not prime")   #2
        break
else:
    print("Number is prime")
