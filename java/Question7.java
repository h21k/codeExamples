package edu.uk.york.practical1;
	import java.io.BufferedReader;
	import java.io.InputStreamReader;
import java.io.FileReader;
	
public class Question7 {

	    public static void main(String[] args) {
	 
	    try {
	 
	         BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	 
	         System.out.println("*********************");
	         System.out.println("***  Datenzugriff ***");
	         System.out.println("*********************");
	 
	         System.out.println("Geben Sie die Art der gewünschten Meldung ein");
	         String Meldung = input.readLine();
	 
	         String aktline = "";
	         BufferedReader inFile = new BufferedReader (new FileReader ("babcom5.txt"));
	         aktline = inFile.readLine();
	        					
	        		String zeile = inFile.readLine();
	        		while (zeile != null) {
	        		  //System.out.println(zeile);
	        			if(zeile.indexOf(Meldung)!= 0){
	        				inFile.readLine();
	        			}
	        		  
	        		}

//	         while (aktline != null)
//	         {
//	        	indexOf(aktline, 0);
//	            if (aktline.contentEquals(Meldung) )
//	            {
//	            System.out.println(aktline);
//	            }
//	            aktline = inFile.readLine();   
//	         }
	         inFile.close();
	 
	    }
	 
	        catch(Exception ex)
	         {
	  System.out.println("Irgendwas ist schief gelaufen !!!");
	 
	  System.out.println(ex.getMessage() );
	 
	       }
	 
	        // TODO code application logic here
	    }
	 
	}