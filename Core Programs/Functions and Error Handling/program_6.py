def Natural(n):
    if (n==1):
        return 1
    sum = Natural(n-1) + n

    return sum

print(Natural(4))