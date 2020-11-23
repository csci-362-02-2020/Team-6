package testcasesexecutables;
import java.awt.Color;
import project.src.ColorConverter;

//this is the TestRGB2Hex class:
//This class tests the rgb2Hex method from the ColorConverter class
public class TestRGB2Hex{
	//this is the main class used to be testing Tanaguru's rgb2Hex where
	//Arguments: ColorRedValue ColorGreenValue ColorBlueValue ExpectedResult TestCaseFilePath
	public static void main(String[] args){
	int[] colorNum = new int[3];
  	for (int i=0;i<3;i++) {
  		colorNum[i] = Integer.parseInt(args[i]);
  		
  	}
    //create new color object:
    Color color1 = new Color(colorNum[0], colorNum[1], colorNum[2]);
    String result = ColorConverter.rgb2Hex(color1);
    //result had to start at index 1 (2nd position) because the # was giving issues when doing comparison:
   //fault: replace result = result.substring(1, result.length()); to result = result.substring(0,result.length());
  //this will not return he ctorrect expectedOutcome.
    result = result.substring(1, result.length());
	String expectedOutcome = args[3];
	String outputFile=args[4];  	
	//Test result output:
	String output=String.valueOf(result)+"\n";
	if (expectedOutcome.contentEquals(result)){
  		output+="Pass";
  	}	
  	else{
  		output+="Fail";
	}
	TestOutput.replaceLines(outputFile,output);
    }
}//end TestRBG2Hex
