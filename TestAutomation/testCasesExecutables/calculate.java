
import java.awt.Color;

public final class DistanceCalculator {

    private static final int CUBIC = 3;
    private static final int ROUND_VALUE = 100;
    
    private DistanceCalculator() {
    }

    /**
     * 
     * @param colorToChange
     * @param colorToKeep
     * @return the calculated distance between 2 colors regarding the 
     * distance definition that can be found here 
     * http://en.wikipedia.org/wiki/Euclidean_distance#Three_dimensions
     */
    public static double calculate(Color colorToChange, Color colorToKeep) {
        return (double) Math.round(Math.abs((Math.cbrt(Math.pow(Double.valueOf(colorToChange.getRed()) - Double.valueOf(colorToKeep.getRed()), CUBIC)
                + Math.pow(Double.valueOf(colorToChange.getGreen()) - Double.valueOf(colorToKeep.getGreen()), CUBIC)
                + Math.pow(Double.valueOf(colorToChange.getBlue()) - Double.valueOf(colorToKeep.getBlue()), CUBIC)))) * ROUND_VALUE) / ROUND_VALUE;
    }
    
    public static void main(String[] args) {
    	int[] colorNum = new int[6];
    	for (int i=0;i<6;i++) {
    		colorNum[i] = Integer.parseInt(args[i]);
		System.out.println(colorNum[i]);
    	}
    	
    	Color joey = new Color(colorNum[0], colorNum[1], colorNum[2]);
    	Color reid = new Color(colorNum[3], colorNum[4], colorNum[5]);
    	System.out.println(calculate(joey, reid));
    	
    }
}
