import copy

#Que1--> Reverse the whole list using list methods.
l=[1,2,3,4,5]
#1st Method:
l.reverse()
print(l)
#2nd Method:
l=[1,2,3,4,5]
print(l[::-1])
print()


#Que2-->Print all the uppercase letters from a string.
a="Hi my name is Bandita"
print("UPPERCASE LETTERS FROM STRING ARE:")
for i in a:
    if i.isupper():
        print(i)
print()


#Que3-->Split the user input on comma's and store the values in a list as integers.
a=input("enter something")
b=(a.split(","))
c=[]
for i in b:
    c.append(int(i))
print(c)
print(type(c[1]))
print()

#Que4-->Check whether a string is palindromic or not.
"""a string is palindrome if its reverse and the original string both are same"""
a=input("enter a string")
b=a[::-1]
if a==b:
    print("yes it is palindrome")
else:
    print("no it is not palindrome")
print()

#Que5-->Make a deepcopy of a list and write the difference between shallow copy and deep copy.
l_1=[1,2,[3,4],5]
l_2=copy.deepcopy(l_1)
l_1[2][0]=6
print(l_1)
print(l_2)

"""deep copy and shallow copy are used for copying data between objects and
The difference between deep copy and shallow copy is that
in shallow copy if original object contains any reference to mutable
objects,then the duplicate reference variable will be created pointing to old content object
but no duplicate objects get started
whereas in case of deep copy is that if original object contains any refernce
to mutable objects,then only the original object is changed after making any chnage to it
but the duplicate object created remains the same i.e. the the copied list remains
same as the original list created but the original list gets updated"""
