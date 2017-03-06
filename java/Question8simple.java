package edu.uk.york.practical1;

import java.io.*;

public class Question8simple {

	public static void main(String[] args){
	 try {
	FileWriter outFile = new FileWriter("output.txt");
	PrintWriter out = new PrintWriter(outFile);
        
// Also could be written as follows on one line
        // Printwriter out = new PrintWriter(new FileWriter(args[0]));
	    
       // Write text to file
		out.println("This is line 1");
		out.println("This is line 2");
		out.print("This is line3 part 1, ");
        out.println("this is line 3 part 2");
	         out.close();
       } catch (IOException e){
           e.printStackTrace();
    }System.out.println("done");
}
}
