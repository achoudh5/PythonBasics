#A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2

import math
class AB:
    def mn(self):
        print "hi"
        x = 0
        print type(x)

        y = 0
        while True:
            a=raw_input("Enter the direction").split(' ')
            print a[0]
            print a[1]
            print "lo"
            if a[0]== 'Up':
                print"hl"
                x+= int(a[1])
            elif a[0]=='down' :
                print "h3"
                x-=int(a[1])
            elif a[0]=="left":
                print "lol"
                y+=int(a[1])
            elif a[0]=="right":
                print "ll"
                y-=int(a[1])
            print x
            print y
            print "ye lo"
            print int(math.sqrt((x**2)+(y**2)))
            str= raw_input("Do you want to continue,y/n\n")
            if str!="y":
                break






def main():
    m=AB()
    m.mn()
if __name__== "__main__":
    main()