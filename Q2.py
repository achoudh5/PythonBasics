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