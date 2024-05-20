# name = input("Enter a user_name ")
# char = input("Enter a char. ")

name,char=input("Enter a name and char. ").split(",")

print(f"Length of your name is {len(name)} ")

print(f"Count of char. you enter is {name.count(char)}")
