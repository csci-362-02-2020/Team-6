#Run from inside TestAutomation directory
import os
path=os.getcwd()
os.system("javac -cp . /project/src/* /testcasesexecutables/*")
testDirectory="/testCases"
for root, dirs, files in os.walk("/testCases"):
  for name in files:
    os.system(commandReturn(testDirectory+"/"+name))

def commandReturn(fileNamePath):
  