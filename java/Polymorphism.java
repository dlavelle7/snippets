public class Polymorphism {
	
	public static void main(String[] args) {
		// Create an Array of Animal types
		Animal[] zoo = new Animal[2];
		zoo[0] = new Dog();
		zoo[1] = new Cat();
		
		// Leverage polymorphism to delegate to the specific types
		for (Animal animal : zoo){
			animal.talk();
		}
	}

}

class Animal {
	
	public void talk(){
		System.out.println("Animal says: Grunt!");
	}
	
}

class Cat extends Animal {
	
	public void talk(){
		System.out.println("Cat says: Meow!");
	}

}

class Dog extends Animal {
	
	public void talk(){
		System.out.println("Dog says: Ruff Ruff!");
	}

}
	


