# modify number gussing game
import random
winning_number= random.randint(1,100)
attempts=0
f=0
i=0
while True:
    n = int(input("Enter a number "))
    attempts +=1
    if (n==winning_number):
        print(f"you win !!! it took {attempts} times")
    elif(n<winning_number):
        print("too low")
    else:
        print("too high")
