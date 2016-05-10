/* 
   Examples of using 'this'

   Run with nodejs
*/

// TODO: Finish and tidy (JSLint?)
// TODO: JavaScript assert?

// 1. Global context
this.spam = "eggs";

console.log("Example #1:", this);

// 2.1 Function context
//function getThis(){
//    // The value of this not set by call, defaults to global
//    return this;
//}
//
//// FIXME: This is false in nodejs????
//console.log(this === getThis())

// 2.2 Function context with strict mode
function strictGetThis(){
    // In strict mode, this remains as whatever it
    // is set to during execution context (undefined here)
    "use strict"
    return this;
}

console.log("Example #2.2:", strictGetThis() === undefined)

// 2.3 Function context with bind()
function spam(){
    return this.spam;
}

// Bind creates a new function same as the bound
// function, but this is the first arg of bind()
var foo = spam.bind({"spam": "foo"})

console.log("Example #2.3:", foo() === "foo");
