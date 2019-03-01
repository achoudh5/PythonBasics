#Q25

class A:
    def ashu(self):
        dict=[1,2,3,4,56,7,8,9,10]

        z= map( lambda x:x**2 , filter(lambda x: x%2==0,dict) )
        print z
def main():
    l = A()
    l.ashu()


if __name__=="__main__":
    main()


