try:
    a= int(input("Enter 1st no. : "))
    b= int(input("Enter 2nd no. : "))
    c = a/b 
    print ("a/b = " + str(c))
# except Exception as e:
except ZeroDivisionError:
    print("Infinite")