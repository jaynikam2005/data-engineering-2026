#String CodeBlocks

#String
a='nana'

#multi-line string
a_more='''Hello Nana..!
how are you..?'''  

#Count length of letters in a string
print(len(a))
print(len(a_more))

#Accessing the characters in a string from their index
print(a[0:])  #from index 0 (From starting character to the end) to the last index
print(a_more[:28]) #from starting index to the desired index i.e 28 here

#Methods/Functions (default/user-defined) associated with string
print(a.lower())  #lowercase the whole string eg.'NANA' to 'nana'
print(a.upper())  #uppercase the whole string eg.'nana' to 'NANA'
print(a.count('a'))  #It iterates through whole string and counts the no of characters passed as a argument
print(a.find('n'))  #It returns the index of the first occurence of the character passed as a argument 
print(a.replace('n','k'))  #It replaces all the occurences of the first character with the second character passed as a argument
print('{} {} ..welcome! {}'.format('Hello','Bhiaya ji','nono'))  #String concatenation using format function (Most efficient way to concatenate strings)
a= 'hello' + 'nana'  #String concatenation using + operator (Very Basic way to concatenate the strings)
a=f"{a} {a_more.upper()} Welcome..!"  #String concatenation using the f-strings ()
print (a)

print(dir(a))  #It shows all possible methods/functions associated with the string/int/float/any data types
print(help(str))  #it shows the description of all the methods/functions associated with the passed data type i.e string here (str) we can pass int/float/any data type too


#Interger/Floats CodeBlocks

c=-3
d=5.55
print(type(a))  #It checks the data type of the passed argument
print(abs(c))  #It returns/prints the absolute value of the passed argument i.e here -3 becomes 3
print(round(d))  #It rounds off the float value to the nearest possible integer value
print(round(d,1))  #It will round off the given argument to the specified decimal places i.e 1 here  

#Casting - It converts one data type into the another
e='10' # Here e and f both are string data types
f='20'
e=int(e) # Here we are converting the e and f string data types to the integer data types
f=float(f)


#Sets,Lists,Tuppels CodeBlocks:

#Lists

L=['banana','apple','mango']  #Defining a list.
M=[]   #Defining an empty list.
print(L)  #Printing a list

#To check length of a list
print(len(L))
print(len(M))

#To get the specific index
print(L[1])
#print(M[1]) #It will throw an error cause list is empty
print(L[-1])  #This gives the last index of the list (Best way to get the last element of any list without knowing the length of the list)

#Adding elements to a list
M.append('Pompom')  #It adds the element at the last index of the list (We can only add one element at a time using append function)
print(M)

M.insert(0,'arts') #It will add the element at the specified index i.e 0 here and shifts the rest of the elements to the right
print(M)

M.extend(L) #It adds all the elements from the specified list to the existing list
M.extend(['Apple','banana'])  #We can add multiple elements to a specified string using the extend function

#Remove elements from a list

L.remove('mango')  #It remove the specified element from the list i.e we passed the mango here 
print(L)

K=L.pop() #It removes the last element from the list
print(K) #It will show the popped element
print(L) #It will show the list after popping the last element

#Sorting a list
L.reverse()  #It prints the list in reverse order
print(L)
L.sort() #It sorts the list in alphabetical order / ascending order for numbers]
print(L)
L.sort(reverse=True) #It sorts the list in descending order
print(L)

J=sorted(L)
print(J)  #It prints the sorted list in ascending order without changing the original list ( Good method to sort a list without changing the original list)

#Functions for the list
print(min(L))  #It prints the minimum value in the list (for strings its based on alphabetical order)
print(max(L))  #It prints the maximum value in the list (for strings its based on alphabetical order)
print(sum([1,2,3,4,5]))  #It prints the sum of all the int/float values in the passed list argument

#Finding the index of a element in a list
print(L.index('banana'))  #It will print the index of the specified element passed as an argument

print('arts' in M)  #It checks whether the specified element is present in the list or not and returns the boolean value accordingly

#Index with values
for i in enumerate(L):
    print(i)  #It prints the index along with the values of the list as tuple pairs o/p: '0,banana' , '1,apple' etc

for i in enumerate(L,start=1):
    print(i) #It prints the index along with the values of the list as tuple pairs starting from the specified index i.e 1 here o/p: '1,banana' , '2,apple' etc
    
#Join method  : List --> String
L=['banana','apple','mango']
S=', '.join(L)  #It joins all the elements of the list to form a string with the specified separator i.e ', ' here
print(S)

#Split method : String --> List
A=S.split(', ') #It splits the string into a list based on the specified sepaartor i.e '- ' here
print(A)


#Tupples
t1=('a','b','c')  #Defining a tupple
t2=()  #Defining an empty tupple
print(t2) #Printing the tupples
print(t1)
#t1[0]='e'  #It will throw an error cause tupple does not support item assignment (It is called immutability)



#Sets : Order changes on each execution cause unlike list and tupples sets dont care about order , It also checks if the element is part of the set or not before adding it (No duplicate values allowed)
s1={'a','b','c','m','n'}  #Defining a set 
#s2={}  #This is not a set , it is a dictionary
s3=set()  #This is a proper empty set 

#To check if item is present in the set or not (We can do this for Lists and Tupple also but Sets are optimized for such operations)
print('a' in s1)  #It checks whether the specified passed element is present in the set or not and return a boolean value accordingly i.r True/False

'''Most Importantly Sets can do is to check if the value is being shared or not shared with the other Sets'''

#To check if item is present in both or not
s4={'m','n','o','p'}
print(s1.intersection(s4)) #It will print the common elements between both the sets i.e 'm' and 'n' here

#To check if elements are in Set1 but not in Set2
print(s1.difference(s4))  #It will print the elements which are in Set1 but not in Set2 i.e 'a','b','c' here

#Combining/Concatination of sets
print(s1.union(s4))   #It will combine both the sets and print all the unique elements from both the sets (No repeated elements)


""" List,Tupples, Sets Summary:
Lists : Ordered , Mutable (Can be changed) , Allows Duplicates
Tupples : Ordered , Immutable (Cannot be changed) , Allows Duplicates  
Sets : Unordered , Mutable (Can be changed) , No Duplicates Allowed
 
List:
empty_list=[]
empty_list=list()


Tupple:
empty_tupple=()
empty_tupple=tupple()


Sets:
empty_sets={}   #This is not a set , it is a dictionary
empty_set=set()  #This is a proper empty set

"""


#Dictionary CodeBlocks : It allows us to do work with key-value pairs , i.e word - key or defination - value

d1={'name':'Jay','age':25,'height':172.2,'Class':"B.Tech"}  #Defining a dictionary with key-value pairs
print(d1)

#If we want the svalue of the specific key
print(d1['name'])  #It will print the value of the specified key i.e 'name' here it will o/p: 'Jay'
#print(d1['Phone'])  #If we try to access the value for the key that is not present in the dictionary it will throw an error

#Accessing value with get() method
print(d1.get('age'))  #It will print the value of the specified key i.e 'age' here it will o/p: 25
print(d1.get('Phone'))  #If we try to access the value for the key that is not present in the dictionary it will return 'None' instead of throwing an error cause of get() method

#we can pass the default value for those key's which are not present in the dictionary using get() method
print(d1.get('Phone','Not_found'))  #It will print Not_found instead of None as we have passed the default value for the key 'Phone' which is not present in the dictionary

#Adding new entry to the dictionary
d1['Phone'] ='55555-5555'
print(d1) 

#Update values using update() method
d1.update({'age':26,'height':173.5,'City':'Dhule'})  #It will update the existing key's value and can add new key-value pairs too to the existing dictionary
print(d1)

#Delete a key-value pair from the dictionary using del keyword
del d1['Class']
print(d1)

#Delete a key-value pair using pop() method : It can delete and grab the value of the deleted key too
d1_pop=d1.pop('City')
print(d1_pop)  #It will print the value of the deleted key i.e 'Dhule' here
print(d1)   #It will print the dictionary after deleting the key-value pair

#Looping through all key value pairs in the dictionary

#To see how many keys we have in the dictionary
print(len(d1))  #It will print the no of key-value pairs present in the dictionary

#To see all the keys in the dictionary using keys() method
print(d1.keys())   #It will print all the keys present in the dictionary o/p: dict_keys(['name', 'age', 'height', 'Phone'])

#To see all the values in the dictionary using the values() method
print(d1.values())  #It will print all the values present in the dictionary o/p: dict_values(['Jay', 26, 173.5, '55555-5555'])

#To see all the key-value pairs in the dictionary using items() method
print(d1.items())  #It will print all the key-value pairs present in the dictionary as tuple pairs o/p: dict_items([('name', 'Jay'), ('age', 26), ('height', 173.5), ('Phone', '55555-5555')])

#Looping

#To get all the keys
for i in d1:
    print(i)  #It will print all the keys present in the dictionary

#To get all the keys and values
for i in d1.items():
    print(i)  #It will print all the key-value pairs present in the dictionary as tuple pairs

#To get all the values in the dictionary
for i,j in d1.items():
    print(j)  #It will print all the values present in the dictionary



#Conditional Statements , Booleans CodeBlocks: If,Else and Elif Statements  (Object identification test if both objects have same id or not)

#False values examples : None , 0 , 0.0 , '' (empty string) , [] (empty list) , () (empty tupple) , {} (empty dictionary) , set() (empty set),False are considered as False values in Python


#Loops and Iterations CodeBlocks: For and While Loops

#Break : It immediately terminates the loop and comes out of it
#Continue : It skips the current iteration and moves to the next iteration of the loop

#Loop within loop : Nested Loops

#Range: If we want to rin the loop for specific no of times we can use range function
for i in range(5):
    print(i)  #It will print from 0 to 5 (5 Items)

for i in range(1,11): #First argument is starting index and second argument is ending index +1
    print(i)  #It will print from 1 to 10 (10 Items) 

#While Loop : Ot just keep looping till the specified condition is True, We have to break it
c=0
while c<5:
    print(c) #It will stuck in infinite loop as we are not incrementing the value of c so it will always be less than 5
    c+=1   #Increamenting the value of c to avoid infinite loop



#Functions CodeBlocks: Defining and Calling Functions
def nana(a):
    pass  #We use this when we dont have to do anything in the function but syntactically we have to write something in the function body later

def add(b):
    return b  #If there are no arguments passed in the function the o/p is None by default
print(add())  # o/p:None

#calling a function

nana(5)  #Function is called with the argument in it 

''' Changing only the content in the function is called as "Dry" Which means dont repeat yourself '''

#Return makes the function more powerful as it can return values back to the caller
print(add(5))  # If we use the print the return statement becomes string and we can perform string operations on it

#If we passed arguments in a function

def b(c,d):
    return '{} b'.format(c+d)  #It will return the concatenated string of c and d with ' b' at the end
print(b(5,6))  #It will o/p: 11 b

# '''If we somewhere'''

'''
def fun(*args,**kargs):  #args and kargs are just variable names we can use any other names too
    print(args)
    print(kargs)
#args=tuple
#kargs=dictionary
'''
def fun(*args,**kargs):  
    print(args)
    print(kargs)
    return "Done"
print(fun('arts','maths','science',name='Jay',age=25,height=172.5))

'''
O/P:
('arts', 'maths', 'science')
{'name': 'Jay', 'age': 25, 'height': 172.5}
Done

'''


#If we made a tuple and dictionary separately and try to access them using the positional arguments

T=('Arts','Commerce','Science')
D={'name':'jay','age':25,'height':173.5}
print(fun(*T,**D))

'''
O/P:
('Arts', 'Commerce', 'Science')
{'name': 'jay', 'age': 25, 'height': 173.5}
Done

'''



#Importing Modules and Exploring Standard Library CodeBlocks:

'''
Syntax:

import module_name  #It imports the whole module under a short name
import module_name as mn  #It imports the whole module under a short name mn here
from module_name import func_name  #It imports only the specified function from the module


from module_name import *  #It imports all the functions from the specified module (It is generally not recommended to use this method as it can create confusion in case of same function names in different modules)

'''
import sys  #It imports the sys module to run below function/method
print(sys.path)  #It shows where python is looks for the modules to import


'''We can actually add directory of module to give system where to find the module

import sys
sys.path.append(/path)

'''


#Standard Library Modules:

#random Module: Module to access random items
import random
a=random.choice('apple')  #It will choose a random character from the passed string argument
print(a)

#math Module: Module to do basic mathematical operations
import math
b=math.sin((90))   #It will convert 90 degrees to radians and then calculate the sin value of it
print(b)

#datetime Module: This allows to work with date and time
import datetime
t=datetime.date.today()  #It will print today's date
print(t)

#calendar Module: This allows to work with calendars
import calendar
print(calendar.isleap(2026))  #We have to pass the year to check whether it is leap year or not , It will return boolean value accordingly

#os Module: Gives us the access to the underlying operating system functionalities
import os
print(os.getcwd())  #It gets the current working directory path

'''If we used

import Module_name
print(Module_name.__file__)
 
It will print the path where the module is located in the system
'''