'''
***      n=3
**
*              
'''

def print_pattern(n):
    if n==0: return 1

    print("*"*n)
    return print_pattern(n-1)

print_pattern(3)