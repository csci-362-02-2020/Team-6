package testcasesexecutables;
import java.awt.Color;
import project.src.DistanceCalculator;


public class TestCalculate {

    public static void main(String[] args) {
    	int[] colorNum = new int[6];
    	for (int i=0;i<6;i++) {
    		colorNum[i] = Integer.parseInt(args[i]);
    	}
    	
    	Color joey = new Color(colorNum[0], colorNum[1], colorNum[2]);
    	Color reid = new Color(colorNum[3], colorNum[4], colorNum[5]);
    	System.out.println(DistanceCalculator.calculate(joey, reid));
    }
}