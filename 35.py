class Circle:
    def rec(self,n):
        print "hi"
        print "wassup"
        y=[1,3,2,6,4,9,7]
        y1=sorted(y)
        print y1
        for i in y1:
            #print i
            if i==n:
                print y1.index(i) # using the element to find the index
            else:
                print "element not found"
                break
def main():
    l = Circle()

    # j=NewYorker()
    n = int(raw_input("enter the number:\n"))
    l.rec(n)
if __name__=="__main__":
    main()