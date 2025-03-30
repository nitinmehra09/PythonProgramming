
# l = command for check you are on which line
# n = command for run that line
# q = command for quit 
# c = command for continue

# for example
import pdb
pdb.set_trace()
name = input("Enter your name : ")
age = input("Enter your age : ")

print(f"Your name is {name} and your age is {age}")
age2 = age + 5 
print(f"your name is {name} and your age is {age2}")
