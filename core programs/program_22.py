n=input("Enter a number containing more than one digit ")
sum=0
i=0
while i<len(n):
    j=int(n[i])
    sum=sum+j
    i+=1

print(f"sum of {n[0]}+{n[1]}+{n[3]}+.... is {sum}")