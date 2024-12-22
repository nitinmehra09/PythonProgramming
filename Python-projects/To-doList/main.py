l = []

while True:
    print("Enter your Choice : ")
    print("1. Add Tasks\n2. Delete Tasks\n3. Veiw All Tasks\n4. Exit ")
    Choice = int(input("Enter your choice : "))
    try:
        if Choice == 1:
            tasks = input("Enter the task : ")
            l.append(tasks)
        elif Choice == 2:
            index = int(input("Enter index of task you want to delete : "))
            l.remove(l[index-1])
        elif Choice == 3:
            print("Your Tasks are : ")
            for i in range(0,len(l)):
                print(l[i])
        elif Choice == 4:
            print("Thank You !!!")
            break
        else:
            print("Enter a valid Choice ")
    except Exception as e:
        print(e)