#Write a program that computes the value
# of a+aa+aaa+aaaa with a given digit as the value of a.

class A:
    def q15(self):
        a=raw_input("Enter the number\n")
        n1= int(a*1)
        n2= int(a*2)
        n3= int(a*3)
        n4=int(a*4)
        print n1,n2,n3,n4
        print (n1+n2+n3+n4)

# If you don't use int, then the output will just be concatenated because it's a string
#        n1 = int(a * 1)
#        n2 = (a * 2)
#        n3 = (a * 3)
#        n4 = (a * 4)
#        print n1, n2, n3, n4
#        print (n1 + n2 + n3 + n4)


def main():
    y=A()
    y.q15()

if __name__=="__main__":
    main()