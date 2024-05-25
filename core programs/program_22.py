n=input("Enter a number containing more than one digit ")
sum=0
i=0
while i<len(n):
    j=int(n[i])
    sum=sum+j
    i+=1

a = "+".join(n)

print(f"sum of {a} is {sum}")