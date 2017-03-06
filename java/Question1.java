package edu.uk.york.practical1;
import java.lang.Math;

public class Question1 {

	/**
	 * @param args
	 * 
	 * 
	 * Write and test a luckyDip() method that uses repetition to generate and display 6 random numbers for the National
		*Lottery. The display should be of the format:
		*Ball 1 = 23
		*Ball 2 = 16
		*etc
	 */
	static void luckydip( int c){
		
		int balls = 1;
		String s;
		while(balls <= c){
			s = "Ball Nr."
					+ balls
					+ "="
					+ (int)(Math.random()*100); //+1
			System.out.println(s);
			balls += 1;
		}

	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String x = ("Hi, Welcome to the Computer Science Lottery!");
		String z = ("How many balls would you like to use in the lottery?");
		System.out.println(x);
		System.out.println(z);
		int input = Integer.parseInt(args[0]); 
		luckydip(input);


	}
}
