#Run from inside TestAutomation directory
import os
import sys

def commandReturn(fileNamePath):
  fName = open(fileNamePath, 'r')
  for i,line in enumerate(fName):
    if i==3:
        return line.strip()
  fName.close()
        
def testCaseRead(fileNamePath):
  fName = open(fileNamePath, 'r')
  fName.close()

if(len(sys.argv)==2 and sys.argv[1]=="c"):
  os.system("javac -cp . project/src/* testcasesexecutables/*")
path=os.getcwd()
testDirectory="testCases"
reportDirectory="reports"
for root, dirs, files in os.walk(testDirectory):
  for name in files:
    os.system(commandReturn(testDirectory+"/"+name)+" "+os.path.abspath(testDirectory+"/"+name))


    