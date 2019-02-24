#Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.

class A:
    def ashu(self):
        print "hi"

        while True:

            a=raw_input("enter thestrings\n").split(' ')
            #for i in a:
            d={i: a.count(i) for i in a}
            str= raw_input("Do you want to continue: y/n\n")
            if str != 'y':
                break

        print d


def main():
    l=A()
    l.ashu()


if __name__=="__main__":
    main()

