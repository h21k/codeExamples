package edu.uk.york.practical1;

public class Cat extends Animal{
	
	public Cat(String s, int x) {
		super(s, x);
		// TODO Auto-generated constructor stub
	}
	private int lives = 9;

	public void getLives(){
		System.out.println(lives);
	}
	public void setLives(int e){
		lives = e;
		if(lives == 0){
			System.out.println("Oh noes! The Cat is dead!");
		}
	}
	public void looseLives(){
		lives --;
		if(lives == 0){
			System.out.println("Oh noes! The Cat is dead!");
		}
	}
    /*public String toString(){
		return ("Lives: " + lives + "\n" + "check ");
	}*/

}
