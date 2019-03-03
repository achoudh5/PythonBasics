import random
from random import shuffle
import zlib
import sys
import timeit
class Circle:
    def rec(self):
        a=raw_input("Enter the String")  #strings are immutable
        print a[-2:-6:-1]   #extended slice step...[begin:end:step]
        print a[2:6:-1]   # nothing would be printed, since start and stop finishes before even it reaches to a point to step
        print a[2:6:1]    #begins from the second char and end at the 6th with a default spacing of 1
        print a[::-1]     # prints the string in the reverse order
        print a[::]       # prints what is being entered



def main():
    l = Circle()

    # j=NewYorker()

    l.rec()
if __name__=="__main__":
    main()