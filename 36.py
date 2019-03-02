import random
class Circle:
    def rec(self):
        print "hi"
        print "wassup"
        while True:
            #n = int(raw_input("enter the number:\n"))
            if 60<random.random()*100<100:
                print "hi"
                print random.random()*100   #generates the random numbers from (0,1)
            elif random.randint(5,10):
                print "ji"
                print random.randint(5,10)  # generates random numbers within the integer frame
            else:
                print "lp"
                str= raw_input("Do you want to continue: y/n\n")
                if str != 'y':
                    break

def main():
    l = Circle()

    # j=NewYorker()

    l.rec()
if __name__=="__main__":
    main()