package testcasesexecutables;
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.FileReader;

//This class is for writing the results for each test cas
public class TestOutput{
	//Method only replaces (or adds) the last 2 lines of the testCase file to display results according to test case template
	//Arguments: OutputFile Output
	//Output newLine expected to already be properly formatted for append
    public static void replaceLines(String filename,String newLine){
        try{
        	BufferedReader file=new BufferedReader(new FileReader(filename));
        	String line;
        	String lines="";
        	int count=0;
			//Reads the file through line 5 to keep the data, but not old test results (if any exist)
			while ((line = file.readLine()) != null && count<6) {
            		lines+=line+"\n";
            		count++;
        	}
        	file.close();
        	FileWriter fileOut=new FileWriter(filename);
        	fileOut.write(lines+newLine);
        	fileOut.close();
        }
        catch (Exception e) {
        	System.out.println("Problem reading file.");
    	}
    }
}