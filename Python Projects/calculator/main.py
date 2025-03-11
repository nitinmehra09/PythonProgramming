while True:
    print("Enter opration : ")
    print("1. addition \n2. substaction \n3. multiply \n4. division")
    operation = int(input("Enter operation : "))
    if operation >0 and operation <5:
        a = float(input("Enter 1st number : "))
        b = float(input("Enter 2nd number : "))
        if operation == 1:
            print(f"{a} + {b} = {a+b}")
        elif operation == 2:
            print(f"{a} - {b} = {a-b}")
        elif operation == 3:
            print(f"{a} X {b} = {a*b} ")
        elif operation == 4:
            print(f"{a}/{b} = {a/b}")
    else:
        print("Invalid Input!!!")
        break