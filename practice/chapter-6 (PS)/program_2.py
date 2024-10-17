subject1 = int(input("Enter marks in subj1 : "))

subject2 = int(input("Enter marks in subj2 : "))

subject3 = int(input("Enter marks in subj3 : "))

percentage =(subject1+subject2+subject3)/300

if (subject1>33 and subject2>33 and subject3>33 and percentage>=40):
    print("Pass")

else:
    print("Fail")


print(percentage)