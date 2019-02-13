#3. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
#such that is an integral number between 1 and n (both included) and then the program should print the dictionary.

def q3(n):
    d={}
    for i in range(1,n+1):
        d[int(i)] = int(i*i)
    print d
a=int(raw_input("Enter a number:"))
q3(a)
