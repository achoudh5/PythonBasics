# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Unable to do without built-in sorted(0

class A:
    def q8(self,b):
        c=[]
        for i in b.split(','):
            d=i.strip()
            print d
            c.append(d)
            while 1:
                for j in range(0,len(c)):
                    print "ko"
                    print c
                    if c[j-1]>c[j]:
                        print c[j-1]
                        print c[j]
                        print "cpme"
                        (c[j-1],c[j])=(c[j],c[j-1])
            print "lop"
            print c


def main():
    a=A()
    b= raw_input("Enter the strings:\n")
    a.q8(b)
if __name__=="__main__":
    main()
