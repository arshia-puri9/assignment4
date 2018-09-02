#REGULAR EXPRESSIONS:
#ques1:
import re
email=input("enter email address")
if re.match("^[a-zA-Z0-9][_a-zA-Z0-9]*(@)(gmail.com|yahoo.com)$",email):
    print("valid email")
else:
    print("not valid id")
#ques2:
import re
num=input("enter number")
if re.match("^[6-9]{1}[0-9]{9}",num):
    print("correct")
else:
    print("incorrect")
