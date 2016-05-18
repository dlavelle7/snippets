/*
    Examples of using Object.prototype

    All objects in javascript descend from Object. All objects inherit methods
    and properties from Object.prototype
*/


// TODO: Finish

// 1. Create a new Prototype using the Object contructor function with
// properties and functions (similar to a class)
function Employee(first, last, age) {
    this.first = first;
    this.last = last;
    this.age = age;
    this.getYearBorn = function(){
        return new Date().getFullYear() - age;
    };
}

// use 'new' keyword to create new objects from the prototype
var joe = new Employee("joe", "bloggs", 30);
console.log("Example #1.1:", joe.first === "joe");
console.log("Example #1.2:", typeof(joe.getYearBorn()) === 'number');

// 2. Add a property and function to an object
var bob = new Employee("bob", "black", 40);
bob.nickname = "bobby";
console.log("Example #2.1:", bob.nickname === "bobby");

bob.formatAge = function(){
    return bob.age + "yrs";
}

console.log("Example #2.2:", bob.formatAge() === "40yrs");

// TODO: Would this be better than console.log()????
// if (bob.nickname !== 'bobby'){ throw "example 1.1 failed";};

// 3. Use the 'prototype' property to add properties and functions to
// existing Prototypes
// Note: Can't do it without 'prototype' property as Prototype is not an object
Employee.prototype.basedIn = "Ireland";
console.log("Example #3.1:", joe.basedIn === "Ireland");

Employee.prototype.fullName = function() {
    return this.first + " " + this.last;
}
console.log("Example #3.2:", joe.fullName() === "joe bloggs");

// 4. "Base" and "sub classes"
// As javascript doesn't have sub class objects, prototype is a workaround
function Manager(first, last, age){
    // pass Manager object to Employee object constructor (as it's this)
    Employee.apply(this, [first, last, age]);
    this.role = "managing";
}
mary = new Manager("mary", "murphy", 50);
console.log("Example # 4.1:", mary.first === "mary");
// FIXME: Doesn't work for Manager but does for Employee
//console.log("Example # 4.2:", mary.fullName() === "mary murphy");
console.log("Example # 4.3:", mary.role === "managing");

// TODO: Object.create()
