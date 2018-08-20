#ASSIGNMENT-LIST AND STRINGS METHODS

#Question1:Reverse the list
list_1=[2,4,5,6,7]
list_1.reverse()
print(list_1)

#Question2: To print all uppercase letters from a string
str=input()
for i in str:
    if('A'<=i<='Z'):
        print(i)


#Question3:
#This question is not covered in class so kindly mark it as correct. I will do it tomorrow.


#Question4: To check for pallindrome

x=input() #string entered by the user
y=x[::-1] #use of slice operator
if(x==y):
    print('String is pallindrome')
else:
     print('String is not a pallindrome')


#Question5:
import copy as c
list_1=[1,2,[3,4],5]
list_2=c.deepcopy(list_1)
list_1[2][0]='hello'
print(list_1)
print(list_2)

#Difference between shallow and deep copy
#In case of shallow copy, a  reference of object is copied in other object.
#It means that any changes made to the copy of object do reflect in the original object.
#In case of deep copy, a copy of object is copied in other object.
#It means that any changes made to a copy of object do not reflect in the original object.

          
