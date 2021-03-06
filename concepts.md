# split()--->
### At some point, you may need to break a large string down
### into smaller chunks, or strings. This is the opposite of concatenation
### which merges or combines strings into one.


# join()--->
### The join() is a string method which returns a string concatenated with the elements of an iterable
### The join() method takes an iterable - objects capable of returning its members one at a time
### Some of the example of iterables are:
### Native datatypes - List, Tuple, String, Dictionary and Set
### File objects and objects you define with an __iter__() or __getitem()__ method

### It only works on strings and not int or any other data type

# tuple=('8','9','3')
### print ','.join(tuple)

```
import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]  # user enter a comma separated value
print items            # returns a list
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print value            # returns a list
print ','.join(value)  #return in comma separated output
```

# 2-D Matrix
```
b= [[i*j for j in range(y)] for i in range(x)]

```

# 3-D Matrix
```
b= [[[i*j*z for j in range(y)] for i in range(x)]for z in range(g)]
```

# ASCII value conversion
```
ord(<enter the char>)
```
# Character to ASCII
```
chr(104)
'h'
```
# Sorting without using sorted() in python
```
a=raw_input("Enter\n")
b=[]

list= [b.append(i) for i in a.split(',') if i not in b]
print b
for i in range(len(b)):
    for j in range(len(b)-1):
        if b[j]>b[j+1]:     #replacing if the condition is true
            b[j],b[j+1]=b[j+1],b[j]
print b
```
# Sorting based on (name,age,number) where I have to give priority to name then age then number

```
from operator import itemgetter, attrgetter

l = []
while True:
    s = raw_input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print sorted(l, key=itemgetter(0,2))
```
# Conversion from Binary to integer and vice-versa

```angular2
a=(raw_input("Enter\n"))
for i in a.split(','):
    i=int(i,2)  # bin to int
    j=bin(i)   # int to binary
    print j[::2]  # omit the '0b' in the bin converted number
    print i
```

# Check if the character is a letter or a digit

## isalpha() ---> The isalpha() returns:
## isaplha() doesn't take any inputs
### True if all characters in the string are alphabets (can be both lowercase and uppercase).
### False if at least one character is not alphabet.

# STRING METHODS

## str.isaplha()--->
### Return true if all characters in the string are alphabetic and there is at least one character, false otherwise

## str.isalnum()--->
### Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise
###  A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().

## str.isdecimal()---> 
### Return true if all characters in the string are decimal characters and there is at least one character, false otherwise.
### ex. "12345½" -->false

## str.isdigit()--->
### Return true if all characters in the string are digits and there is at least one character, false otherwise.
### ex. "12345½"--->false

## str.islower()--->
### Return true if all cased characters [4] in the string are lowercase and there is at least one cased character, false otherwise.

## str.isnumeric--->
### Return true if all characters in the string are numeric characters, and there is at least one character, false otherwise
### ex. "12345½"---> True

## str.strip()--->
### strips off the space left and right of the character or end os sentence

## str.rstrip()--->
### Strips only the right side space only

## str.lstrip()---->
### Strips off the space on the left side only

# Accessing Dictionary

```angular2
s = raw_input()
d={"UPPER CASE":0, "LOWER CASE":0}
print d["UPPER CASE"]  #you can access a particular value like this
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1 # incrementing the value
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print "UPPER CASE", d["UPPER CASE"] #you can access a particular value
print "LOWER CASE", d["LOWER CASE"]
```
```
a=9
n1=int("%s" % a)
print n1
# aa is undefined unless I define like this below
n2= int("%s%s" % (a,a))
print n2
```

# Python Dictionary get()

### dict.get(key[, value])
### The get() method takes maximum of two parameters:

#### key - key to be searched in the dictionary
#### value (optional) - Value to be returned if the key is not found. The default value is None.
#### the value for the specified key if key is in dictionary.
#### None if the key is not found and value is not specified.
#### value if the key is not found and value is specified
### The get() method returns the value for the specified key if key is in dictionary.
```angular2
person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))
```

```
Name:  Phill
Age:  22
Salary:  None
Salary:  0.0
```

### how to reverse the elments of a dict and store in a list
```angular2
res = list((str(v)+' '+ k) for k,v in d.iteritems())
```

### adding values to the dict when in a loop

```angular2
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d={}
        res=[]
        for i in cpdomains:
            #i.split(' ')
            l=(i.split(' '))
            p=l[1].split('.')
           # print p
            #if len(p)>1:
            for j in range(len(p)):
                    #if p[j] in d.keys():
                    p[j]='.'.join(p[j:len(p)])
                    #print p[j]
                    
                    d[p[j]]= d.get(p[j],0)+ int(l[0])  
```
# To print all the combinations in pair
```angular2
print list(itertools.combinations(nums,2))
```
### How to access key, if value is given?
```angular2
for name, age in dictionary.items():    # for name, age in dictionary.iteritems():  (for Python 2.x)
    if age == search_age:
        print(name)
```

# collections.Counter(s)---> where s is a list , gives me a dictionary

# Regex--> Regular Expressions

```
import re
a=raw_input("E:\n").split(',')
for i in a:
    pattern="(\w+)@((\w+.)(.com))"
    g=re.search(pattern,i)
    #r2=re.match(pattern,i)
    print g.group(1)                 # only incase of re.search(), I have duscovered the usage of groups, it gives error incase of re.findall
    p='\d'
    f= re.findall(p,i)               # finds the pattern across the whole text and returns the matches
    print f
``` 
```angular2   
output:
abnsh2@gmail.com
abnsh2
['2']
```


# Error_Handling

### try and except
### example:-
```angular2
try:
    return 5/0
except ZeroDivisionError:
     print "Zero Division Error"
```

# binary search function

```angular2
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index
```

# Compression and Decompression

### Use zlib.compress() and zlib.decompress() to compress and decompress a string.

# Random

```angular2
import random
print random.sample(range(100), 5)  # 2 args second arg is the sample size
```
```angular2
import random
print random.choice([i for i in range(201) if i%5==0 and i%7==0]) # single argument 
```
```angular2

Use random.random() to generate a random float in [0,1].
```

```angular2
import random
print random.randrange(7,16)
```

# 3-D and 2-D array

```angular2
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
```

```angular2
array = [[0 for col in range(8)] for col in range(5)]
```
# Duplicate Elements

```angular2
set1=([1,3,6,78,35,55])
set2=([12,24,35,24,88,120,155])
g=[]
for i in set1:
    for j in set2:
        if i==j:

            g.append(i)

print (g)

set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1 &= set2
li=list(set1)
print li
```

#### Use itertools.permutations() to get permutations of list

# s[::2]---> [start:stop:step]


# Ascii to char and Vice-versa

```angular2
items= ['a','A','Z','z']

for i in items:
    print (ord(i))

    print (unichr(97))
```


# Collections ( to find the most common element and many others)
*http://rahmonov.me/posts/python-collections-counter/*
# Sorting
### Selection Sort

**The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.**

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

*Time Complexity: O(n2) as there are two nested loops.*

**Auxiliary Space: O(1)**

*The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.*

Stability : The default implementation is not stable. However it can be made stable. Please see stable selection sort for details.

In Place : Yes, it does not require extra space.
```angular2
a=[1,2,3,4,5,0,2,1]
        for i in range(0,len(a)):
            for j in range(0,len(a)-1):
                print a[j]
                print "ji"
                if a[j]>a[j+1]:
                    print "ok"
                    a[j],a[j+1]=a[j+1],a[j]
                    print a
```

### Bubble sort
*Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order*
```angular2
a=([10000,300,6,78,35,55])
min= a[0]
#print min
for i in range(len(a)):
    for j in range(len(a)-1-i):
        print "hi"
        print a[j]
        print a[j+1]
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

print a
```
Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

Best Case Time Complexity: O(n). Best case occurs when array is already sorted.

Auxiliary Space: O(1)

Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.

Sorting In Place: Yes

Stable: Yes

# Insertion Sort

First, set a key to the second element of the array.
now, take a pointer j which is one less than the key's index
Until the while conditions are true and key is greater move on otherwise perform the swap the key with the min element set.
Do it until the key is greater than the array element. 
This way perform it until the end

```

def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
        
```

Time Complexity: O(n*2)

Auxiliary Space: O(1)

Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.

Algorithmic Paradigm: Incremental Approach

Sorting In Place: Yes

Stable: Yes

Online: Yes

Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.


# Merge Sort
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
```angular2
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        print arr

mergeSort([1,4,8,3,9])

```

Time complexity of Merge Sort is \Theta(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array in two halves and take linear time to merge two halves.

Auxiliary Space: O(n)

Algorithmic Paradigm: Divide and Conquer

Sorting In Place: No in a typical implementation

Stable: Yes

# How to encode and decode a URL

```angular2
d={}
class Codec:
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        #global d
        d[hash(longUrl)]=longUrl
        return hash(longUrl)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return d[shortUrl]
```
# How to make a list with alternate elements from two different lists

```angular2
b=[]
        c=[]
        for i in range(len(A)):
            if A[i]%2!=0:
                 b.append(A[i])  
            else:
                c.append(A[i])
        #print b
        #print c
        A[::2], A[1::2] = c, b
        return A
        ================OR===============
        list=[]
        while True:
            try:
                list.append(c.pop(0))
                list.append(b.pop(0))
            except IndexError:
                break
        return list
```
# CSV_PARSER

```
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
       ```
# How to Open a file using python lib?

```angular2

import urllib2 
content=urllib2.urlopen("https://wordpress.org/plugins/about/readme.txt") 
for line in content: 
    print (line)
```
# Tree
## Tree_Traversals
class Node(object):
    def __init__(self,value):
        self.value= value
        self.left= None
        self.right= None
 
class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)
    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root," ")
        elif traversal_type == "inorder":
            return self.inorder_print( tree.root, " ")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, " ")
        else:
            print(" Traversal type " + str(traversal_type) + " is not supposed" )
            return False
     def preorder_print(self, start, traversal):
        """Root->Left->Right""" 
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
         return traversal
      def inorder_print(self, start, traversal):
          """Left->Root->Right""" 
          if start:
             traversal = self.inorder_print(start.left, traversal)
             traversal += (str(start.value) + "-")
             traversal = self.inorder_print(start.right, traversal)
           return traversal
      def postorder_print(self, start, traversal):
            """Left->Right->Root"""  
           if start:
                traversal = self.postorder_print(start.left, traversal)
                traversal = self.postorder_print(start.right, traversal)
                traversal += (str(start.value) + "-")
           return traversal
# Lambda Function

```angular2
evenNumbers = filter(lambda x: x%2==0, li
squaredNumbers = map(lambda x: x**2, range(1,21))```

```
# itertools.combinations(iterable, r)

https://docs.python.org/3/library/itertools.html#itertools.combinations
