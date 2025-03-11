'''

email = input("Enter your email : ") #g@g.in
k = 0
d = 0
j = 0
if len(email) >=6:
    if(email[0].isalpha):
        if('@' in email) and (email.count('@')==1):
            if(email[-4]==".")^(email[-3]=="."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif(i.isalpha()): 
                        if i == i.upper():
                            j = 1
                    elif(i.isdigit()):
                        continue
                    elif( i == "_" or i == "." or i == "@"):
                        continue
                    else:
                        d = 1
                if k ==1 or j == 1 or d ==1 :
                    print("Wrong Email ")
                else:
                    print("Right Email ")
        else:
            print("you have to use @ ones in email ")
    else:
        print("first letter of your email is not (1,@,$)")
else:
    print("invalid email ")

'''

# nice version:


email = input("Enter your email: ")  # Example: g@g.in
has_space = False
has_uppercase = False
has_invalid_char = False
if len(email) >= 6:
    if email[0].isalpha():
        if '@' in email and email.count('@') == 1:
            if email[-4] == '.' or email[-3] == '.':
                for char in email:
                    if char.isspace():
                        has_space = True
                    elif char.isalpha() and char.isupper():
                        has_uppercase = True
                    elif char.isdigit():
                        continue
                    elif char in "_@.":
                        continue
                    else:
                        has_invalid_char = True
                if has_space or has_uppercase or has_invalid_char:
                    print("Invalid email. Please ensure no spaces, no uppercase letters, and no invalid characters are present.")
                else:
                    print("Valid email!")
            else:
                print("Invalid email. Ensure the domain ends with '.abc' or '.abcd'.")
        else:
            print("Invalid email. Use exactly one '@' symbol.")
    else:
        print("Invalid email. The first character must be a letter.")
else:
    print("Invalid email. Length must be at least 6 characters.")
