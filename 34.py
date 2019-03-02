class Circle:
    def rec(self,n):
        print "hi"
        print "wassup"

        for i in range(0,n+1):
            if i%5==0 and i%7==0:
                yield i

def main():
    l = Circle()
    y=[]
    # j=NewYorker()
    n = int(raw_input("enter the number:\n"))
    for i in l.rec(n):    # if you try to print yield directly from the function, either it will print an objectID or nothing
        y.append(i)       # Using this way, we can print the value
    print y               # Here, we are calling the function
    # j.printNationality()

if __name__=="__main__":
    main()