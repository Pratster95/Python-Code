def fact_num(n):
    mul=1
    for i in range(n):
        mul=mul*(i+1)
    return mul

n=int(input("Enter the value of n"))
print ("The factorial of",n,"is",fact_num(n))