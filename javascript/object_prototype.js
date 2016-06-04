/*
    Examples of using Object.prototype

    All objects in javascript descend from Object. All objects inherit methods
    and properties from Object.prototype
*/


// 1. Create a new Prototype using the Object contructor function with
// properties and functions (similar to a class)
function Employee(first, last, age) {
    this.first = first;
    this.last = last;
    this.age = age;
    this.getYearBorn = function() {
        return new Date().getFullYear() - age;
    };
}

// use 'new' keyword to create new objects from the prototype
var joe = new Employee('joe', 'bloggs', 30);
console.assert(joe.first === 'joe');
console.assert(typeof(joe.getYearBorn()) === 'number');


// 2. Add a property and function to an object
var bob = new Employee('bob', 'black', 40);
bob.nickname = 'bobby';
console.assert(bob.nickname === 'bobby');

bob.formatAge = function() {
    return bob.age + 'yrs';
};

console.assert(bob.formatAge() === '40yrs');


// 3. Use the 'prototype' property to add properties and functions to
// existing Prototypes
// Note: Can't do it without 'prototype' property as Prototype is not an object
Employee.prototype.basedIn = 'Ireland';
console.assert(joe.basedIn === 'Ireland');

Employee.prototype.fullName = function() {
    return this.first + ' ' + this.last;
};
console.assert(joe.fullName() === 'joe bloggs');


// 4. 'Base' and 'sub classes' in javascript
// As javascript doesn't have sub class objects, prototype is a workaround
function Developer(first, last, age) {
    // pass Developer object to Employee object constructor (as it's this)
    Employee.apply(this, [first, last, age]);
    this.role = 'development';
}
// Create a new Developer prototype object using the 'super' prototype
Developer.prototype = Object.create(Employee.prototype);
// Specify the function that creates a Developer objects prototype
Developer.prototype.constructor = Developer;

mary = new Developer('mary', 'murphy', 50);
console.assert(mary.first === 'mary');
console.assert(mary.fullName() === 'mary murphy');
console.assert(mary.role === 'development');
