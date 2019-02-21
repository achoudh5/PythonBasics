#Write a program that accepts a sentence and
# calculate the number of letters and digits.


class A:
    def tu(self):
        count=0
        count1=0
        p=raw_input("Enter the number and digits\n")
        for i in p.split(' '):
            #print i.isalpha()
            for j in i:
                #print j
                if j.isalpha():
                    #print len(j)
                    count+=len(j)
                    #print count
                elif (j).isdigit():
                    #print j
                    #print len(j)
                    count1+=len(j)
                    #print count1
        print count
        print count1


def main():
    l=A()
    l.tu()


if __name__=="__main__":
    main()