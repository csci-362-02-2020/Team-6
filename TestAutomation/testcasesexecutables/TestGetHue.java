package testcasesexecutables;
import java.awt.Color;
import project.src.ColorConverter;
import testcasesexecutables.TestOutput;

//Class tests the getHue method from the ColorConverter class
public class TestGetHue {
	//Arguments: ColorRedValue ColorGreenValue ColorBlueValue ExpectedResult TestCaseFilePath
	public static void main(String[] args) {
		int[] colorNum = new int[3];
		//turns the string arguments into integers in an array
    	for (int i=0;i<colorNum.length;i++) {
    		colorNum[i] = Integer.parseInt(args[i]);
    	}
    	//creates the color using the parameters from
    	Color color1 = new Color(colorNum[0], colorNum[1], colorNum[2]);
    	//puts the expected Outcome parameter into a usable float value 
    	float expectedOutcome = Float.parseFloat(args[3]);
		String outputFile=args[4];
		//gets the results from the tested method and stores it in a variable
    	float hueValue = ColorConverter.getHue(color1) * 360;
		//Test result output to HTML
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
