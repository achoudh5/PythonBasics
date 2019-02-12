#Q:- What to enter in the function var while calling a function ex. here I have put a random number
#inside q1(0) to call the function, what else can I do?
#Q2: why return gives nothing but print gives me the list output.
def q1(a):
    a=[]
    for i in range(2000,3201):
        if i%7==0 and i%5!=0:
            a.append(i)

    print a
    #return a

#b=raw_input("enter the number")
q1(0)