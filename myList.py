import os
path=os.getcwd()
list=os.listdir(path)
header="<h1>"+path+"</h1>"
f = open("myList.html", "w")
f.write(header+"\n")
f.close()
os.system("browse myList.html")
