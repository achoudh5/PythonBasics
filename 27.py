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
        print 0

class Square(Circle):
    def __init__(self,l):
        self.l=l

    def rec(self):
        print self.l * self.l
def main():
    d=int(raw_input("enter the number"))
    l = Square(d)
    #j=NewYorker()
    l.rec()
    #j.printNationality()


if __name__=="__main__":
    main()


