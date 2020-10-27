package testcasesexecutables;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class TestOutput{
    
    public static void replaceLines(String filename,String newLine){
        try {
            StringBuffer inputBuffer = new StringBuffer();
            Scanner sc=new Scanner(new File(filename));
            int count=0;
            while (sc.hasNextLine()&&count<5) {
                inputBuffer.append(sc.nextLine()+System.lineSeparator());
                count++;
            }
            sc.close();
            FileWriter writer=new FileWriter(filename);
            writer.write(inputBuffer.toString()+"\n"+newLine);
            writer.close();

        } catch (Exception e) {
            System.out.println("Problem reading file.");
        }
    }
}