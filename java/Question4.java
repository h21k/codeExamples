package edu.uk.york.practical1;

public class Question4 {

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
	int u = a / b;
	System.out.println("a"+ "/" + "b" + "=" + u);
}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Enter number 1:");
		//try-catch exception handling....?
		int r = Integer.parseInt(args[0]);
		System.out.println("Enter number 2:");
		int l = Integer.parseInt(args[1]);
		System.out.println("Select Operation:");
		System.out.println("Enter 1 for addition");
		System.out.println("Enter 2 for subtraction");
		System.out.println("Enter 3 for multiplication");
		System.out.println("Enter 4 for division");
		int o = Integer.parseInt(args[2]);
		if(o == 1){
			add1(r,l);
		}else if(o == 2){
			sub1(r,l);
		}else if(o == 3){
			mult1(r,l);
		}else if(o == 4){
			div1(r,l);
		}System.out.println("Operation successful!");
		
	}

}
