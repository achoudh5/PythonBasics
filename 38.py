import random
import zlib
import sys
import timeit
class Circle:
    def rec(self):
        print "hi"
        print "wassup"
        s=timeit.timeit('''def main():  
    l = Circle()

    # j=NewYorker()

    l.rec()''')   #helps in measuring the time
        print s


def main():
    l = Circle()

    # j=NewYorker()

    l.rec()
if __name__=="__main__":
    main()