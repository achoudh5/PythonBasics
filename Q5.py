# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case
# Also please include simple test function to test the class methods.


#Q= when I used A.getString() (in the main program, it gave me an error)
class A:
    def getString(self):
        a=raw_input("enter the string\n")
        print a
    def printString(self):
        print (raw_input("enter the string\n")).upper()

def main():
    A1= A()
    A1.getString()
    A1.printString()

if __name__=="__main__":
    main()
