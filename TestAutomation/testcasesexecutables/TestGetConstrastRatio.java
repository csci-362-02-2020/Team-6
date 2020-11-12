package testcasesexecutables;
import java.awt.Color;
import project.src.ContrastChecker;
import testcasesexecutables.TestOutput;

//Class tests the ContrastChecker class's getConstrastRatio method
//Typo from their code
public class TestGetConstrastRatio {
	//Arguments: Color1RedValue Color1GreenValue Color1BlueValue Color2RedValue Color2GreenValue Color2BlueValue ExpectedResult TestCaseFilePath
    public static void main(String[] args) {
		int[] colorNum = new int[6];
    	for (int i=0;i<6;i++) {
    		colorNum[i] = Integer.parseInt(args[i]);
    	}
		double expectedOutcome = Double.parseDouble(args[6]);
		String outputFile=args[7];
    	double calcValue = ContrastChecker.getConstrastRatio(new Color(colorNum[0], colorNum[1], colorNum[2]), new Color(colorNum[3], colorNum[4], colorNum[5]));
		//Test result output
		String output=String.valueOf(calcValue)+"\n";
		if (expectedOutcome == calcValue){
    		output+="Pass";
    	}
    	else{
    		output+="Fail";
		}
		TestOutput.replaceLines(outputFile,output);
    }
}
