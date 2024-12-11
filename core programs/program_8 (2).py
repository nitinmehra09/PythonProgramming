def inchToCms(inch):
    return inch * 2.54

def cmToInch(cm):
    return cm / 2.54

inch =int(input("Enter lenght in inches: "))
print(f"{inch} inch is equal to {inchToCms(inch)}cm")