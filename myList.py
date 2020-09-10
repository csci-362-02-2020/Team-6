import os
path=os.getcwd()
list=os.listdir(path)
header="<h1>"+path+"</h1>"
f = open("myList.html", "w")
f.write(header+"\n")
f.close()
f = open("myList.html", "a")
for i in list:
    f.write("<p>"+i+"</p>")
f.close()
os.system("browse myList.html")