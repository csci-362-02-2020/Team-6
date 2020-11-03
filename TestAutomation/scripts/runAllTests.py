#Run from inside TestAutomation directory
#Command for compiling: python scripts/runAllTests.py c
#Otherwise: python scripts/runAllTests.py
import os
import sys

def commandReturn(fileNamePath):
  fName = open(fileNamePath, 'r')
  for i,line in enumerate(fName):
    if i==3:
        return line.strip()
  fName.close()
        
def htmlReport(fileNamePath, reportFile):
  rName=open(reportFile,'a')
  locked=True
  while locked:
    fName = open(fileNamePath, 'r')
    testCase=fName.readlines()
    if(len(testCase)!=7):
      fName.close()
      continue
    else:
      locked=False
      rName.write("<h2>"+testCase[0]+"</h2>\n")
      labels=["<b>Tested class: </b>","<b>Tested Method and Parameters: </b>","<b>Command for executable: </b>"]
      testCase[3]+=" "+os.path.abspath(fileNamePath)
      for i in range(1,4):
        rName.write("<p>"+labels[i-1]+testCase[i]+"</p>\n")
      rName.write("<p>"+"<b>Expected Result: </b>"+testCase[4]+"\t"+"<b>Returned Result: </b>"+testCase[5]+"</p>\n")
      rName.write("<p>"+testCase[6]+"</p>\n")
  rName.close()
  fName.close()

if(len(sys.argv)==2 and sys.argv[1]=="c"):
  os.system("javac -cp . project/src/* testcasesexecutables/*")
path=os.getcwd()
testDirectory="testCases"

reportDirectory="reports"
reportFile="reports/testReport.html"
rName=open(reportFile,'w')
rName.write("<h1>Tanaguru TestAutomation Results</h1>")
rName.close()

for root, dirs, files in os.walk(testDirectory):
  for name in sorted(files):
    os.system(commandReturn(testDirectory+"/"+name)+" "+os.path.abspath(testDirectory+"/"+name))
    htmlReport(testDirectory+"/"+name,reportFile)
os.system("browse "+reportFile)