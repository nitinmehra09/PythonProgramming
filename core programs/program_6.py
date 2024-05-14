# num_1 = int(input("Enter 1st number "))
# num_2 = int(input("Enter 2nd number "))
# num_3 = int(input("Enter 3rd number "))
# OR

num_1, num_2, num_3=input("Enter three number : ").split(",")

sum = int(num_1)+int(num_2)+int(num_3)
avg = str(sum/3)

print(f"average of {num_1} , {num_2} and {num_3} is " + avg)

# or  

print("average of {} , {} and {} is {}".format(num_1, num_2, num_3, avg))

