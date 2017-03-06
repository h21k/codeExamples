package edu.uk.york.practical1;

public class Animal {

	private String name;
	private int legs;
	
	public Animal(String s, int x){
		this.name = s;
		this.legs = x;
	}


	public void getName(){
		System.out.println(name);
	}
	public void getLegs(){
		System.out.println(legs);
	}

}
