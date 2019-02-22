# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

#Yield not working
class A:
    def getString(self):
        a= raw_input("enter the number\n")
        for i in range(0, int(a)):
            if (i % 7) == 0:
                print i
                #yield i

def main():
    w= A()
    w.getString()


if __name__=="__main__":
    main()