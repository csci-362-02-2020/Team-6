package testcasesexecutables;
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.FileReader;

public class TestOutput{
    
    public static void replaceLines(String filename,String newLine){
        try{
        	BufferedReader file=new BufferedReader(new FileReader(filename));
        	String line;
        	String lines="";
        	int count=0;
        	while ((line = file.readLine()) != null && count<5) {
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