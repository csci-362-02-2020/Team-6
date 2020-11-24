#Reid Foster, Joe Mezera, Stefan Veloff
#runAllTests.py
#CSCI362, testing framework for Tanaguru Contrast Finder
#11/17/2020

#Run from inside TestAutomation directory
#Command for compiling: python scripts/runAllTests.py c
#Otherwise: python scripts/runAllTests.py

import os
import sys

#This method looks in the test case file and returns the needed command
def commandReturn(fileNamePath):
  fName = open(fileNamePath, 'r')
  testCase=fName.readlines()
  fName.close()
  return "java -cp . "+testCase[3].strip()+" "+testCase[4].strip()+" "+testCase[5].strip()+" "+os.path.abspath(fileNamePath)

#This method appends the report for a test case using the test case template
def htmlReport(fileNamePath, reportFile,lastModified):
  rName=open(reportFile,'a')
  locked=True
  #A lock is made to ensure the file has been updated
  while locked:
    fName = open(fileNamePath, 'r')
    testCase=fName.readlines()
    if(len(testCase)!=8 or lastModified>=os.path.getmtime(fileNamePath)):
      fName.close()
      continue
    else:
      locked=False
      rName.write("<tr>")
      for i in range(0,7):
        rName.write("<td>"+testCase[i]+"</td>")
      #Adds color depending on pass or fail
      if(testCase[7]=="Pass"):
        rName.write("<td style=\"color:green\"><b>"+testCase[7]+"</b></td></tr>")
      else:
        rName.write("<td style=\"color:red\"><b>"+testCase[7]+"</b></td></tr>\n")
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
rName.write("<h1>Tanaguru TestAutomation Results</h1>\n<table style=\"width:100%\" id=\"t01\"><tr><th>Test ID</th><th>Tested class</th><th>Tested Method and Parameters</th><th>Driver</th><th>Arguments</th><th>Expected outcomes</th><th>Last Result from Running Test</th><th>Success or Fail</th></tr>\n")
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
