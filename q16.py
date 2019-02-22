# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.

class A:
    def gh(self):
        k=(raw_input("krde bahi"))
        j=(k.split(','))
        print j
        X= [int(i)**2 for (i) in j if int(i)%2 != 0]
        print X
def main():
    h=A()
    h.gh()

if __name__=="__main__":
    main()