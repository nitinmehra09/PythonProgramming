name = input("Enter your user_name : ")
age =int(input("Enter your age "))

# if (name[0]=='a'or name[0]=='A'):

if (name[0].lower()=='a'):
    if(age>=10):
        print("you can watch coco ")
    else:
        print("your age is below 10 ")
else:
    print("your name not start with 'A' or 'a' so you can not watch coco ")