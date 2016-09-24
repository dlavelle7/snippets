class Person {
	
	String name;
	int age;
	
	// Overloaded constructors
	Person(String name){
		this.name = name;
	}
	
	Person(String name, int age){
		this.name = name;
		this.age = age;
	}
	
	// Overloaded methods
	public void showInfo(){
		System.out.println("My name is " + this.name);
	}
	
	public void showInfo(String message){
		System.out.println(message + "My name is " + this.name);
	}
	
}

class Overloading {

	public static void main(String[] args) {
		// Create two objects using different Person class constructors
		Person sarah = new Person("Sarah");
		Person david = new Person("David", 29);
		// Call overloaded methods
		sarah.showInfo();
		david.showInfo("Overloaded: ");
	}

}