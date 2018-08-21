#DECISION AND FLOW CONTROL

#Question1:

year=int(input("enter year"))
if(year%4==0 and year%100!=0 or year%400==0):
                                             print("Yes it is leap year")
else:
     print("No it is not a leap year")

#Question2:
length=input("enter length")
breadth=input("enter breadth")
if(length==breadth):
    print("It is a square")
else:
    print("It is a rectangle")

#Question3:
p1=input("enter age for first person")
p2=input("enter age for second person")
p3=input("enter age for third person")
#check oldest
if(p1 > p2 and p1 > p3):
    print("p1 is oldest")
elif( p2 > p1 and p2 > p3):
    print("p2 is oldest")
elif (p3 > p1 and p3 > p2):
    print("p3 is oldest")

# check youngest
if (p1 < p2 and p1 < p3):
    print("p1 is youngest")
elif( p2 < p1 and p2 < p3):
    print("p2 is youngest")
elif( p3 < p1 and p3 < p2):
    print("p3 is youngest")

#Question4:
age=int(input("enter age"))
sex=input("enter sex M or F")
ms=input("enter marital status Y or N")
if sex=='F' :
    print("can work only in urban areas")
else:
    if age in range(20,41):
        print("you can work anywhere")
    elif age in range(41,61):
         print("you can work only in urban area")
    else:
         print("error")

        


#Question5:
quan=int(input("enter no of units"))
total=int(quan*100);
if(total>1000):
    dis=(10*total)/100;
    new=total-dis;
    print("Total cost for user is {}".format(new))
else:
    print("Total cost for the user is {}".format(total))


    #LOOPS
#ques1:

for i in range(10):
    num=int(input("enter a number"))
    print(num)

#ques2:
    num=1
while(num==1):
    print("hello")

#ques3:
list=[1,2,3,4]
new=[]
for i in list:
    new.append(i ** 2)
print(new)

#ques4:
list=[2,3.0,'arshia',5,2.2]
l1=[] #list for integers
l2=[] #list for strings
l3=[] #list for float 
for i in list:
    if(type(i)==int):
        l1.append(i)
    elif(type(i)==str):
        l2.append(i)
    else:
        l3.append(i)
        
print(l1)
print(l2)
print(l3)

#ques5:
list=[]
for num in range(1,101):
    for i in range(2,num):
        if(num%2==0):
            break
        else:
            list.append(num)
            break
        
print(list)

#ques6:

for i in range(0,4):
    for j in range(0,i+1):
        print("*",end="")
    print("\n")

#ques7:
list=[1,2,3]
num=int(input("number to search"))
for i in list:
    if(num==i):
        list.remove(num)
        break;
    
print(list)   



    
    

     
    
    
    






    

