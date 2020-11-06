#Run from inside TestAutomation directory
#Command for compiling: python scripts/runAllTests.py c
#Otherwise: python scripts/runAllTests.py
import os
import sys

#This method looks in the test case file and returns the needed command
def commandReturn(fileNamePath):
  fName = open(fileNamePath, 'r')
  for i,line in enumerate(fName):
    if i==3:
        return line.strip()
  fName.close()

#This method appends the report for a test case
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
      rName.write("<tr><td>"+testCase[0]+"</td>\n")
      testCase[3]+=" "+os.path.abspath(fileNamePath)
      for i in range(1,4):
        rName.write("<td>"+testCase[i]+"</td>\n")
      rName.write("<td>"+testCase[4]+"</td>"+"<td>"+testCase[5]+"</td>\n")
      if(testCase[6]=="Pass"):
        rName.write("<td style=\"color:green\"><b>"+testCase[6]+"</b></td>\n")
      else:
        rName.write("<td style=\"color:red\"><b>"+testCase[6]+"</b></td></tr>\n")
      rName.close()
      fName.close()
  

#compiles java files if parameter is met
if(len(sys.argv)==2 and sys.argv[1]=="c"):
  os.system("javac -cp . project/src/* testcasesexecutables/*")
path=os.getcwd()
testDirectory="testCases"
#initializes html report
reportDirectory="reports"
reportFile="reports/testReport.html"
rName=open(reportFile,'w')
rName.write("<head><style>table, th, td {border: 1px solid black;border-collapse: collapse;}</style><style>th, td {padding: 15px;}</style><style>#t01 tr:nth-child(even) {background-color: #eee;}</style><style>#t01 tr:nth-child(odd) {background-color: #fff;}</style><style>#t01 th {color: white;background-color: black;}</style></head>\n")
rName.write("<h1>Tanaguru TestAutomation Results</h1>\n<table style=\"width:100%\" id=\"t01\"><tr><th>Test ID</th><th>Tested class</th><th>Tested Method and Parameters</th><th>Command for executable</th><th>Expected outcomes</th><th>Last Result from Running Test</th><th>Success or Fail</th></tr>\n")
rName.close()
#walks through each test case
for root, dirs, files in os.walk(testDirectory):
  for name in sorted(files):
    lastModified=os.path.getmtime(testDirectory+"/"+name)
    os.system(commandReturn(testDirectory+"/"+name)+" "+os.path.abspath(testDirectory+"/"+name))
    htmlReport(testDirectory+"/"+name,reportFile,lastModified)
rName=open(reportFile,'a')
rName.write("</table>")
rName.close()
os.system("browse "+reportFile)