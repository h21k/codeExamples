package edu.uk.york.practical1;

public class Question3 {

	int store;
	
	static int generateRandom(){
	int a = (int)(Math.random()*100);
	return a;
}
	static void guess(int store, int input){
		int a = input;
		if(a > store){
			System.out.println("High!");
		}else if(a < store){
			System.out.println("Low!");
		}System.out.println("Hit! You've got it!");
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//int store = 0;
		int store = (int)(Math.random()*100);
		int input = Integer.parseInt(args[0]);
		generateRandom();
		guess(store,input);
		System.out.println("hi!");
		//System.out.println(a);
		
		
	}

}
