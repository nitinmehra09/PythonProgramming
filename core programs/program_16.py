#if, else and elif 


name = input("enter your name ")
age = int(input("enter your age "))

if (0<age<=3):
    print("Ticket price : free ")
elif(3<age<=10):
    print("Ticket price : 150")
elif(10<age<=60):
    print("Ticket price : 250")
elif(age>60):
    print("ticket price : 200")
else:
    print("please enter a valid age ")
