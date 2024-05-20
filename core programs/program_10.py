name,char=input("Enter a name and char. ").split(",")

print(f"Length of your name is {len(name)} ")

print(f"Count of char. you enter is {name.strip().lower().count(char.strip().lower())}")

