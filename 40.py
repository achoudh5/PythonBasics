import random
from random import shuffle
import zlib
import sys
import timeit
class Circle:
    def rec(self):

        a=[12,24,35,70,88,120,155]
        array = [0,4,5]
        print [y for x,y in enumerate(a) if x not in array]

        z=timeit.timeit('''class Circle:
    def rec(self):

        
        print [y for x,y in enumerate([12,24,35,70,88,120,155]) if x not in (0,4,5)]




def main():
    l = Circle()

    # j=NewYorker()

    l.rec()
if __name__=="__main__":
    main()''')
        print z


def main():
    l = Circle()

    # j=NewYorker()

    l.rec()
if __name__=="__main__":
    main()