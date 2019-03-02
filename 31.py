from math import *
import re
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
            pattern='(\d)'
            r2=re.findall(pattern,l) #finding all the patterns in the sentence or argument
            print r2




def main():

    l = Circle()
    #j=NewYorker()
    l.rec()
    #j.printNationality()

if __name__=="__main__":
    main()


