#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

class A:
    def q10(self):
        b= raw_input("enter the string")
        c=[]
        d=[]
        for i in b.split(' '):
            print i
            if i in c:
                continue
            else:
                c.append(i)
        #print c

        while c:
            minimum = c[0]  # arbitrary number in list
            for x in c:
                if x < minimum:
                    minimum = x
            d.append(minimum)
            c.remove(minimum)

        print ' '.join(d)





def main():
    a= A()
    a.q10()

if __name__=="__main__":
    main()


