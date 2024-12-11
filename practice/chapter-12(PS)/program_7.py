n = int(input("Enter a no. : "))
l = [i*n for i in range(1,11)]
with open("tables.txt","a") as f:
    f.write(f"Table of {n} ----> "+str(l)+ "\n")
