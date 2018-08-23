#FUNCTIONS
#ques1:
def area(radius):
    '''To calculate area of sphere'''
    ar=4*3.14*radius**2;
  
    return(ar)
radius=int(input("enter radius"))
z=area(radius)
print(z)

#ques2:
def perfect(n):
     l=[]
     for i in range(1,n):
         if n%i==0:
             l.append(i)
     if sum(l)==n:
          return True
for i in range(1,1001):
    if perfect(i):
        print(i,"is a perfect number")
             
#ques3:
def table(n):
    '''to calculate table of a number'''
    for i in range(1,11):
        print(n*i)
n =int(input("enter no"))
table(n)
       
#ques4:
def pow(b,exp):
    if(exp==1):
        return(b)
    if(exp!=1):
        return(b*pow(b,exp-1))
b=int(input("enter base"))
exp=int(input("enter exponential"))
print("answer:",pow(b,exp))
    


   
    
    
