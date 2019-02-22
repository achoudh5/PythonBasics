#Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.

class A:
    def array(self):
        #print "hi"
        h=['0','2','4','6','8']
        k=[]
        b = (raw_input("Enter the bin numbers:"))

        for i in b.split(','):
            o=len(i)
            print o
            print "kya haal hai wahan"
            ""
            count = 0
            #print "hi"
            for j in range(0, len(i)):
                t=i[j]
                #print type(t)
                if t in h:
                    #print "kl"
                    #print i[j]
                    count+=1
            print count
            if o==count:
                print "lo"
                k.append(i)
        print ' '.join(k)
        #print (b)
        #print (format(raw_input("Enter the nimber:\n"), b)

def main():
    L= A()
    L.array()
if __name__== "__main__":
    main()