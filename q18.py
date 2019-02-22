#A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
#Following are the criteria for checking the password:
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#1. At least 1 letter between [A-Z]
#3. At least 1 character from [$#@]
#4. Minimum length of transaction password: 6
#5. Maximum length of transaction password: 12

class A:
    def gh(self):
        ro = raw_input("Enter the password:\n").split(',')
        print ro
        S = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
        E = 'abcdefghijklmnopqrstuvwxyz'
        K = '0123456789'
        L = '$#@'

        Q = [S, E, K, L]
        c1=c2=c3=c4=0


        for j in ro:
            V = len(j)
            if V in range(6, 13):
                for i in j:
                    if i in S:
                        c1+=1
                        #print "one check passed"
                    elif i in E:
                        c2+=1
                        #print "second check passed"
                    elif i in K:
                        c3+=1
                        #print "third check passed"
                    elif i in L:
                        c4+=1
                        #print "fourth check passed"
                    else:
                        continue
                if c1>0 and c2>0 and c3>0 and c4>0:
                    print (" The password %s is successfully written" %  j)
                else:
                    print "one of the req is missing in password in %s" % j
            else:
                print "length of the password is less than 6 OR greater than 12"
def main():
    h=A()
    h.gh()

if __name__=="__main__":
    main()