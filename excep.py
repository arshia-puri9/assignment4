#Exception handling
#ques1:
#The exception occured is zero division error
try:
    a=3
    if a<4:
           a=a/(a-3)
           print(a)
except ZeroDivisionError:
    print("you cannot divide by zero")

#ques2:
#The exception occured is out of range error
try:
    l=[1,2,3]
    print(l[3])
except ValueError:
    print("error value")
except IndexError:
    print("Error index")
except:
    print("Error")
#ques3:
#An exception is thrown and error occurs

#ques4:
#Output of this program is:
#AbyB(2.0,3.0) evaluates to c=-5.0.hence the else part is executed and -5.0 is printed
#AbyB(3.0,3.0) evaluates to c=6.0/0.0. so the exception is thrown and "a/b result in 0"
    

#ques5:

try:
    import strinng   
    l=[1,2]
    print(l[4])
    s1=input("enter a string")
    s1.isupper()
    print(s1)
    n=int(input("enter a number"))
except IndexError:
    print("index error")
except ImportError:
    print("import error")
except ValueError:
    print("value error")
    


