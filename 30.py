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
            pattern='(\w+)@((\w+\.))+((com|net|edu))'
            r2=re.match(pattern,l)
            print r2.group(3)




def main():

    l = Circle()
    #j=NewYorker()
    l.rec()
    #j.printNationality()

if __name__=="__main__":
    main()


