import random
class Circle:
    def rec(self):
        print "hi"
        print "wassup"
        while True:
            n = int(raw_input("enter the number:\n"))
            if 9<random.random()*100<100:
                print random.random()*100
            else:
                str= raw_input("Do you want to continue: y/n\n")
                if str != 'y':
                    break
def main():
    l = Circle()

    # j=NewYorker()

    l.rec()
if __name__=="__main__":
    main()