#Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
#D 100
#W 200
#--D means deposit while W means withdrawal.
class A:
    def gh(self):
        print "hi"
        total_D=0
        while True:
            # W1=int(raw_input("enter the withdrawl amount\n"))
            D1 = (raw_input("enter the deposit amount\n"))
            c,n=D1.split()
            if c == 'D':
                total_D += int(n)
            else:
                total_D -= int(n)
            str=raw_input("want to continue:")
            if not (str[0]== "Y" or str[0]=="y"):
                break

        print total_D
def main():
    h=A()
    h.gh()

if __name__=="__main__":
    main()
