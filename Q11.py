#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
# and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence

class A:
    def array(self):
        print "hi"
        b = (raw_input("Enter the bin numbers:"))
        for i in b.split(','):
            #print i
            f= int(i, 2)
            print type(f)
            if f%5==0:
                print i

        #print (b)
        #print (format(raw_input("Enter the nimber:\n"), b)

def main():
    L= A()
    L.array()
if __name__== "__main__":
    main()