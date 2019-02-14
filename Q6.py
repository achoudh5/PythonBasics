#Write a program that calculates and
# prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H: C is 50. H is 30.
#D is the variable whose values should be input to your program
# in a comma-separated sequence.


from math import sqrt
class Formula:
    def hitit(self):
        C=50
        H=30
        a=[]
        D= (raw_input("enter the D:\n"))
        for i in D.split(','):
            #print int(i)
            Q= int(sqrt((2*C*int(i)/H)))
            a.append(Q)
        print ",".join((map(str,a)))
def main():
    A=Formula()
    A.hitit()

if __name__== "__main__":
    main()