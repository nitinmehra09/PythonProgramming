n = int(input("Enter a number :"))
i=10
while i>0:
    print(f"{n} X {i} = {i*n}")
    i-=1

print("*************************************")
# using for loop

for i in range(1,11):
    print(f"{n} X {11-i} = {(11-i)*n}")