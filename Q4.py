#4.Write a program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number.

##Q: How to optimize the code here
def q4(a):
    b=[]
    for i in a:
        b.append(i)
        if i==',':
            #print "hi"
            b.remove(i)
    print b
a= raw_input("enter the numbers:")
q4(a)