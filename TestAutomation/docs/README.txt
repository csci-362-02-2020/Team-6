Run from inside TestAutomation directory
To run framework:
    python scripts/runAllTests.py
To recompile Java files:
    python scripts/runAllTests.py c
The python script will run through the testCases directory, running each.  At the end, a report will open in a browser showing the results.
The script will compile any Java files not currently compiled automatically.  To delete the class files and recompile the Java files, add the "c" parameter.

To see the injected faults and how to implement them, view the injectedFaults.txt file