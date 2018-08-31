#COMMON MODULES IN PYTHON
#ques1:
from datetime import datetime
now=datetime.now()
print(now.strftime("%a"))

#ques2:
import webbrowser
url=input("enter search video")
webbrowser.open_new_tab('http://youtube.com/search?q=%s'%a)

#ques3:
import os
path= '/Users/spuri/Desktop/assignments/directory'
f = os.listdir(path)
i=1

for file in f:
    fn=input("enter file name")
    os.rename(os.path.join(path,file),os.path.join(path,fn+'.jpg'))
    i=i+1
