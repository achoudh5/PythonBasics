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
    def rec(self,l):
        x= 5/ (l)
        print x
try:
    d = int(raw_input("enter the number"))
    l=Circle()
    l.rec(d)
except ZeroDivisionError:
    print "number divided by zero"
finally:
    print "learn this"


#def main():
#   d=int(raw_input("enter the number"))
#    l = Circle()
    #j=NewYorker()
#    l.rec(d)
    #j.printNationality()


#if __name__=="__main__":
#    main()


