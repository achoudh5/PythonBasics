#Write a program that accepts a sentence and calculate the number of upper case
# letters and lower case letters.

class A:
    def flow(self):
        count=0
        f=raw_input("Enter the sentence")
        for i in f.split(' '):
            for j in i:
                if j.isupper():
                    count+=1
        print count


def main():
    a=A()
    a.flow()

if __name__=="__main__":
    main()