#FILE HANDLING
#ques1:
n=int(input("enter no of lines to read"))
f=open('f1.txt','r')
data=f.readlines()
for i in range(0,n):
    print(data[i])
f.close()

#ques2:
file=open('f1.txt','r')
data=file.read()
wo=data.split()
ds={}
for word in wo:
    ds[word]=wo.count(word)
print(ds)
file.close()
print()
    
#ques3:
f1=input('enter filename1')
f2=input('enter filename2')
fo=open(f1,'r')
data=fo.read()
fo.close()
fs= open(f2,'a')
fs.write(data)
fs.close()

#ques4:
f1=open('f1.txt','r')
f2=open("f2.txt",'r')
for l1,l2 in zip(f1,f2):
    f3=open("f3.txt",'a')
    f3.write(l1+l2)
    f3.close()
f1.close()
f2.close()
print()

#ques5:
with open('f1.txt','w') as f:
   for i in range(10):
      x=int(input("Enter number: "))
      f.write("%d "%(x))

with open('f1.txt','r') as f:
   data=f.readlines()
   for nu in data:
       l=nu.split()
   l.sort()

with open('f2.txt','w') as f:
   for i in l:
      f.write("%s "%(i))
