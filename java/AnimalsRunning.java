package edu.uk.york.practical1;

public class AnimalsRunning {

	public static void main(String[] args) {
		// TODO Auto-generated method stub


			Animal a1 = new Animal("Spider", 8);
			Dog d1 = new Dog("Shepperd", 4);
			Cat c1 = new Cat("Black and Dangerous!", 5);
			// using the Default Object.toString() Method
			System.out.println("Object toString() method : " + a1);
			// implicitly call toString() on object as part of string concatenation
			String s = a1 + " testing";
			System.out.println(s);
			a1.getName();
			d1.getName();
			d1.getETime();
			d1.setTime(5);
			d1.getETime();
			c1.getName();
			c1.getLives();
			c1.setLives(7);
			c1.looseLives();
			c1.getLives();
			//c1.toString();
			
			
			// BufferedReader, you can use the following statement.

			// import java.io.*;
			// BufferedReader in=new BufferedReader(new InputStreamReader(System.in));

			// String name=in.readLine();

			// Alternatively, you can use Scanner class.

			// import java.util.*;
			// Scanner sc=new Scanner(System.in);
			// String name=sc.nextLine();

			
		
		
	}

}
