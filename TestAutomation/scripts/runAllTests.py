#Run from inside TestAutomation directory
import os
path=os.getcwd()
os.system("javac -cp . /project/src/* /testcasesexecutables/*")
testDirectory="/testCases"
for root, dirs, files in os.walk(testDirectory):
  for name in files:
    os.system(commandReturn(testDirectory+"/"+name)+">>"+testDirectory+"/"+name)

def commandReturn(fileNamePath):
  with fName = open(fileNamePath, 'r')
    for 4,line in enumerate(fName):
    