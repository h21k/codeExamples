package edu.uk.york.practical1;

public class Question2a {
	
	static void generateTable(int f){
		System.out.println("Welcome! See the table!");
		for(int i=1;i<=f;i++){

			for(int j=1;j<=f;j++){

				System.out.print(" "+i*j+" ");

			}
			System.out.print("\n");
		}
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Please instert the number:");
		int f = Integer.parseInt(args[0]);
		generateTable(f);
		System.out.println("Thank you - finished!");
	}

}
