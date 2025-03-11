import random
import string

def generatePassword(lenght):
    char = (string.ascii_letters + string.digits + string.punctuation)
    password = ''.join(random.choice(char) for i in range(lenght))
    return password

lenght = int(input("Enter lenght of password you want : "))
print("Your password is :", generatePassword(lenght))

