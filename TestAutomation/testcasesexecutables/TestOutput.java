package testcasesexecutables;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileOutputStream;

public class TestOutput{
    
    public static void replaceLines(String filename,String newLine){
        /*try {
            StringBuffer inputBuffer = new StringBuffer();
            Scanner sc=new Scanner(TestOutput.class.getResourceAsStream(filename));
            int count=0;
            while (sc.hasNextLine()&&count<5) {
                inputBuffer.append(sc.nextLine()+System.lineSeparator());
                count++;
            }
            sc.close();
            System.out.println(inputBuffer.toString());
            FileWriter writer=new FileWriter(new File(TestOutput.class.getResource(filename).getFile()));
            writer.write(inputBuffer.toString()+"\n"+newLine);
            writer.close();

        } catch (FileNotFoundException e) {
            System.out.println("Problem reading file.");
        }*/
        try{
        	BufferedReader file=new BufferedReader(new FileReader(filename));
        	//StringBuffer inputBuffer=new StringBuffer();
        	String line;
        	String lines="";
        	int count=0;
        	while ((line = file.readLine()) != null && count<5) {
            		lines+=line+"\n";
            		//inputBuffer.append('\n');
            		count++;
        	}
        	file.close();
        	//String inputStr = inputBuffer.toString();
        	//FileOutputStream fileOut=new FileOutputStream(filename);
        	FileWriter fileOut=new FileWriter(filename);
        	fileOut.write(lines+newLine);
        	fileOut.close();
        }
        catch (Exception e) {
        	System.out.println("Problem reading file.");
    	}
    }
}