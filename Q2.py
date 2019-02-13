# 2. Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line.
def fact(n):

    if n==0:
        return False
    elif n==1:
        return 1
    else:
        prod = 1
        for i in range(n):
            prod=prod*n
            n=n-1
    return prod

a=int(raw_input(("enter the number")))
fact(a)