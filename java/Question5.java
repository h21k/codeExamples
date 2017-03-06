package edu.uk.york.practical1;

import java.io.*;

	public class Question5 { 
		
				public static void add1(int a, int b){
				int u = a + b;
				System.out.println("a"+ "+" + "b" + "=" + u);
			}
			public static void sub1(int a, int b){
				int u = a - b;
				System.out.println("a"+ "-" + "b" + "=" + u);
			}
			public static void mult1(int a, int b){
				int u = a * b;
				System.out.println("a"+ "*" + "b" + "=" + u);
			}
			public static void div1(int a, int b){
				double u = a / b;
				System.out.println("a"+ "/" + "b" + "=" + u);
			}	
			
			
		public static void main( String[] args ){
				
			String s1 = new String("add1");
			String s2 = new String("sub1");
			String s3 = new String("mult1");
			String s4 = new String("div1");
			
		        try
		        {
		            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		            String userInput = in.readLine();
		            System.out.println("\n\nUser entered -> " + userInput);
		            
		            		        if( userInput.equalsIgnoreCase(s1)){
		            		        	System.out.println("hit");
		        }
		        }
		        catch(IOException e)
		        {
		            System.out.println("IO Exception - Please enter an operation first then the numbers ");
		        }
		        

		        
		    }
		
	}
	
	
