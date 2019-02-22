#You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
#1: Sort based on name;
#2: Then sort based on age;
#3: Then sort by score.
#The priority is that name > age > score

##Discuss
class A:
    def b(self):
        final = []
        while True:
            d=raw_input("Enter name,age,score\n").split(',')
            print d[0]
            print type(d[0])
            print d[1]
            print d[2]
            #if type(d[0]) != 'str':
            #    print "Name is not entered"
            #    break
            #else:
            final.append((d[0],d[1],d[2]))
            print final
            str= raw_input("Do you want to conitnue: y/n \n")
            if str =="y":
                continue
            else:
                break
        for i in range(len(final)):
            min = final[0][0]
            print min
            if final[i][0]<min:
                min=final[i][0]
                print min
                print "jk"
            elif final[0][0]==final[i][0]:
                min1=final[0][1]
                if final[i][1]<min1:
                    min1=final[i][1]
                    print "case2"
                    if final[0][1]==final[i][1]:
                        min2=final[0][2]
                        if final[i][2]<min2:
                            min2=final[i][2]
                            print "case3"
        print final
def main():
    a=A()
    a.b()
if __name__== "__main__":
    main()
