#Q25

class A:
    def ashu(self):
        dict=[]
        for i in range(1,21):
            dict.append(i)
        z= list(filter(lambda x: x%2==0,dict))
        print z
def main():
    l = A()
    l.ashu()


if __name__=="__main__":
    main()


