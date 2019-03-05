
from text import *
f = open('53.py', 'r')
keyword= raw_input('Enter the employee name:\n')
list=['Anshul','Nikhil','Vaishnavi']
while True:
    text = f.readline()
    if keyword in text:
        print dict[keyword]
        break
    else:
        print "Employee not found"


        # raw_input("enter the keyword")
