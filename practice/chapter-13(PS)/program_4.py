# Write a program to filter a list of numbers which are divisible by 5. 
def DivisibleByFive(n) :
    if(n%5==0):
        return True
    return False 

a = [5,10,30,35,6,5,44,22,76,75]   
 
only_mul_of_five = list(filter(DivisibleByFive,a))

print(only_mul_of_five)