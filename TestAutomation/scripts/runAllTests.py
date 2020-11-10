#Run from inside TestAutomation directory
#Command for compiling: python scripts/runAllTests.py c
#Otherwise: python scripts/runAllTests.py
import os
import sys

#This method looks in the test case file and returns the needed command
def commandReturn(fileNamePath):
  fName = open(fileNamePath, 'r')
  command=""
  for i,line in enumerate(fName):
    if i==3:
        command=line.strip()
  fName.close()
  #Notation used to indicate to the script that a direct filepath to the file is needed
  command=command.replace("[direct filepath]",os.path.abspath(fileNamePath))
  return command

#This method appends the report for a test case using the test case template
def htmlReport(fileNamePath, reportFile,lastModified):
  rName=open(reportFile,'a')
  locked=True
  #A lock is made to ensure the file has been updated
  while locked:
    fName = open(fileNamePath, 'r')
    testCase=fName.readlines()
    if(len(testCase)!=7 or lastModified>=os.path.getmtime(fileNamePath)):
      fName.close()
      continue
    else:
      locked=False
      rName.write("<tr><td>"+testCase[0]+"</td>")
      testCase[3]=testCase[3].replace("[direct filepath]",os.path.abspath(fileNamePath))
      for i in range(1,6):
        rName.write("<td>"+testCase[i]+"</td>")
      #Adds color depending on pass or fail
      if(testCase[6]=="Pass"):
        rName.write("<td style=\"color:green\"><b>"+testCase[6]+"</b></td>")
      else:
        rName.write("<td style=\"color:red\"><b>"+testCase[6]+"</b></td></tr>\n")
      rName.close()
      fName.close()
  

#compiles java files if c argument is passed
if(len(sys.argv)==2 and sys.argv[1]=="c"):
  os.system("javac -cp . project/src/* testcasesexecutables/*")
#Variable names are used to allow alteration to system structure
testDirectory="testCases"
#initializes html report
reportFile="reports/testReport.html"
#Initializes (or rewrites) testReport file with html and css formatting information
rName=open(reportFile,'w')
rName.write("<head><style>table, th, td {border: 1px solid black;border-collapse: collapse;}</style><style>th, td {padding: 15px;}</style><style>#t01 tr:nth-child(even) {background-color: #eee;}</style><style>#t01 tr:nth-child(odd) {background-color: #fff;}</style><style>#t01 th {color: white;background-color: black;}</style></head>\n")
rName.write("<h1>Tanaguru TestAutomation Results</h1>\n<table style=\"width:100%\" id=\"t01\"><tr><th>Test ID</th><th>Tested class</th><th>Tested Method and Parameters</th><th>Command for executable</th><th>Expected outcomes</th><th>Last Result from Running Test</th><th>Success or Fail</th></tr>\n")
rName.close()
#walks through each test case
for root, dirs, files in os.walk(testDirectory):
  for name in sorted(files):
    lastModified=os.path.getmtime(testDirectory+"/"+name)
    os.system(commandReturn(testDirectory+"/"+name))
    htmlReport(testDirectory+"/"+name,reportFile,lastModified)
#Finishes html file and opens in browser
rName=open(reportFile,'a')
rName.write("</table>")
rName.close()
os.system("browse "+reportFile)