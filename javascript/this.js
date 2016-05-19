/*
    Examples of using 'this'
*/


// 1. Global context
this.spam = 'eggs';

console.log('Example #1:', this['spam'] === 'eggs');

// 2 Function context
// 2.1 Simple call
function getThis() {
    // The value of this not set by call, defaults to global
    return this;
}

// Nodejs doesn't have a window object
if (!(typeof(window) === 'undefined')) {
    console.log('Example #2.1:', this === getThis());
    console.log('Example #2.1:', window === getThis());
}

// 2.2 Function context with strict mode
function strictGetThis() {
    // In strict mode, this remains as whatever it
    // is set to during execution context (undefined here)
    'use strict';
    return this;
}

console.log('Example #2.2:', strictGetThis() === undefined);

// 2.3 Function context with bind()
function camelot() {
    return this.spam;
}

// Bind creates a new function same as the bound
// function, but its 'this' is the first arg of bind()
var foo = camelot.bind({'spam': 'foo'});

console.log('Example #2.3:', foo() === 'foo');

// 2.4 An object method
var obj = {
    value: 'bar',
    foo: function() {
        return this.value;  // here 'this' refers to the object
    }
};

console.log('Example #2.4:', obj.foo() === 'bar');

// 2.5 Using call() and apply()
function multiply(var1, var2) {
    return this.foo + var1 + var2;
}

var that = {foo: 'foo'};

// The first argument will be the functions 'this' object,
// the subsequent args will be passed to the function
var res = multiply.call(that, 'bar', 'baz');
console.log('Example#2.5:', res === 'foobarbaz');

// apply() works the same, but function arguments are passed as array
var res = multiply.apply(that, ['bar', 'baz']);
console.log('Example#2.5:', res === 'foobarbaz');
