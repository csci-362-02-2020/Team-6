package testcasesexecutables;
import java.awt.Color;
import project.src.ColorConverter;
import testcasesexecutables.TestOutput;
	
public class TestOffsetRGBColor {

	public static void main(String[] args) {
		int[] colorNum = new int[9];
		//takes the String parameters and turns them into ints and stores them in an array
	   	for (int i=0;i<colorNum.length;i++) {
	    	colorNum[i] = Integer.parseInt(args[i]);
	   	}
	    //creates the color to be changed
	   	Color color1 = new Color(colorNum[0], colorNum[1], colorNum[2]);
	   	//adds the expected outcome results to an integer array
	   	int[] expectedOutcome = new int[]{colorNum[6], colorNum[7], colorNum[8]};
		String outputFile=args[9];
		//changes the Color color1 by the offset amounts set in the test case
	   	color1 = ColorConverter.offsetRgbColor(color1, colorNum[3], colorNum[4], colorNum[5]);
	   	stores the results of the offset in an integer array
	   	int[] result = new int[]{color1.getRed(), color1.getGreen(), color1.getBlue()};
		//Test result output to HTML
		String output=String.valueOf(color1.getRed()+" "+color1.getGreen()+" "+color1.getBlue())+"\n";
		int counter=0;
		for(int i=0;i<3;i++){
			if (expectedOutcome[i] == result[i]){
	   			counter++;
	   		}
	   	}
	   	if (counter ==3){
	   		output+="Pass";
	   	}
	   	else{
	   		output+="Fail";
		}
		TestOutput.replaceLines(outputFile,output);
	   	
	}
}
