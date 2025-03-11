def Temp(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in f : "))
c = Temp(f)
print(f"{f} feranite is equal to {round(c,2)} °C")