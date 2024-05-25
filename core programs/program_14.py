#nested if else 

winning_number=16

n = int(input("guess a number between 10 to 50 : "))

if n==winning_number:
    print("YOU WIN!!!")

else:
    if n>winning_number:
        print("Too high")

    else:
        print("Too low")