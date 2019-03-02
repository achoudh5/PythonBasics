from math import *
class Circle:

    #@staticmethod
    def __init__(self):
        #dict=[]
        #for i in range(1,21):
        #   dict.append(i)
        #print dict
        #self.radius=radius
        pass
    def rec(self):
        y = []

        while True:
            l = (raw_input("enter the number"))
            if '@' in l:
                x = l.split('@')[0]
                y.append(x)
            else:
                print "we need an email address"
            str = raw_input("Do you want to enter another string")
            if str == "yes":
                continue
            else:
                break
        print y



def main():

    l = Circle()
    #j=NewYorker()
    l.rec()
    #j.printNationality()

if __name__=="__main__":
    main()


