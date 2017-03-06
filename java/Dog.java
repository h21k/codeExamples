package edu.uk.york.practical1;

public class Dog extends Animal{
	
	public Dog(String s, int x) {
		super(s, x);
		// TODO Auto-generated constructor stub
	}
	private int excerciseTime = 0;

	public void getETime(){
		System.out.println(excerciseTime);
	}
	public void setTime(int e){
		excerciseTime = e;
	}
}
