package testcasesexecutables;
import java.awt.Color;
import project.src.ColorConverter;
import testcasesexecutables.TestOutput;

public class TestGetHue {
	
	public static void main(String[] args) {
		int[] colorNum = new int[3];
    	for (int i=0;i<colorNum.length;i++) {
    		colorNum[i] = Integer.parseInt(args[i]);
    	}
    	
    	Color color1 = new Color(colorNum[0], colorNum[1], colorNum[2]);
    	
    	float expectedOutcome = Float.parseFloat(args[3]);
		String outputFile=args[4];
    	float hueValue = ColorConverter.getHue(color1) * 360;
		//Test result output
		String output=String.valueOf(hueValue)+"\n";
		if (expectedOutcome == hueValue){
				output+="Pass";
		}
		else{
			output+="Fail";
		}
		TestOutput.replaceLines(outputFile,output);	
	}
}
