#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

#Q: first method problem !! Class A
class A:
    def q9(self,a):

        b=""
        g=a.split()
        for i in g:
            print i
            if ord(i) not in range(65,91):
                c= ord(i) - 32
                b+=chr(c)
            elif ord(i) in range(65,91):
                b += i

        print (" ".join(b))

class B:
    def q92(self,a):
        g=a.split()
        v=[]
        for i in g:
            f=i.upper()
            v.append(f)
        print ' '.join(v)

def main():
    l=A()
    a = raw_input("enter the string :\n")
    #l.q9(a)
    p=B()
    p.q92(a)


if __name__=="__main__":
    main()

