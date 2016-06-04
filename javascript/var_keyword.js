/*
    Examples of using the 'var' keyword and javascripts 'strict mode'.

    The var keyword declares a variable and optionally instantiates it with a
    value. Declared variables are constrained to the context in which they are
    declared (function or global). Undeclared variables are global variables
    (properties of the global object). It is recommended to declare variables.
*/


function eggs() {
    foo = 'foo'; // global variable
    var bar = 'bar'; // declared variable in scope of function 'eggs()'
}

eggs();

// 1. After eggs() is called, global variable 'foo' is created
console.assert(foo === 'foo');

// 2. Variable 'bar' is only declared in the context of 'eggs()'
try {
    console.log(bar);
}
catch (error) {
    console.assert(error.name === 'ReferenceError');
}

// 3. Declared variables are created before any code is executed
var spam;
console.assert(spam === undefined);

// 4. Undeclared variables do not exist until they are assigned a value
try {
    console.log(undeclared_var);
}
catch (error) {
    console.assert(error.name === 'ReferenceError');
}

// 5. Declared variables are non configurable
var im_declared = 10;
delete im_declared; // Fails silently

console.assert(im_declared === 10);

// 6. Undeclared variables are configurable
im_undeclared = 20;
delete im_undeclared;

try {
    console.log(im_undeclared);
}
catch (error) {
    console.assert(error.name === 'ReferenceError');
}

// 7. 'var Hoisting' As declared variables are created before any code is
// executed (see 1.3), variables can be declared after they are assigned values
blah = 1;
var blah; // Declarations done first, not a global anymore
delete blah; // now fails silently (declared vars are non configurable)

console.assert(blah === 1);
