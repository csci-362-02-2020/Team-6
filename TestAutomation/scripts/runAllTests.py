#Run from inside TestAutomation directory
import os

def commandReturn(fileNamePath):
  fName = open(fileNamePath, 'r')
  for i,line in enumerate(fName):
    if i==3:
        return line.strip()
  fName.close()
        
def testCaseRead(fileNamePath):
  fName = open(fileNamePath, 'r')
  fName.close()

path=os.getcwd()
os.system("javac -cp . project/src/* testcasesexecutables/*")
testDirectory="testCases"
reportDirectory="reports"
for root, dirs, files in os.walk(testDirectory):
  for name in files:
    print(commandReturn(testDirectory+"/"+name)+" "+os.path.abspath(testDirectory+"/"+name))
    os.system(commandReturn(testDirectory+"/"+name)+" "+os.path.abspath(testDirectory+"/"+name))


    