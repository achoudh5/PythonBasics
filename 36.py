import random
import zlib
import sys
class Circle:
    def rec(self):
        print "hi"
        print "wassup"
        s="hello world!hello nnnnnworld!hello world!hello world!"
        t=zlib.compress(s,1)
        print sys.getsizeof(s)
        print sys.getsizeof(t)
        print t
        print zlib.decompress(t)
        f=open('34.py','r')
        text=f.read()
        f.close()               #you have to close the files(memory leakage might be there)

        with open('34.py','a') as d:  #better way to open files since you don't have to close file

            print "these are the fice"
            bio=d.read()
        print bio

def main():
    l = Circle()

    # j=NewYorker()

    l.rec()
if __name__=="__main__":
    main()