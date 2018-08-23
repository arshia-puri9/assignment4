#DICTIONARY

#ques1:
n=int(input("number of items you want to enter"))
d={} #empty dictionary
for i in range(n):
    data=input().split()
    d[data[0]]=data[1]
print(d)    

#ques2:
n=int(input("enter no of students"))
d={}
d1={}
for i in range(n):
    d1={}
    name=input("enter name")
    for j in range(n):
        subject=input("enter subject")
        marks=int(input("enter marks"))
        d1[subject]=marks
        d[name]=d1
print(d)
name=input("enter name to see marks")
print(d[name])
