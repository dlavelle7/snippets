/*
    Examples of using JavaScripts 'strict mode'

    Strict mode makes the folowing changes to normal JavaScript behaviour.
    Strict mode applies to entire scripts or individual functions. Strict mode
    is declared by using the 'use strict'; literal expression
*/

// 1. Strict mode for scripts
// Make entire script strict mode by placing literal expression at the
// begining of a script (before any other statements).

// 'use strict';
// foo = 'foo'; // This would cause a Reference error (foo not defined)

// 2. Strict mode for functions
// Put the statement in the functions body before any of its statements invoke
function withStrict() {
    'use strict';
    bar = 'bar'; // throws a ReferenceError, bar not defined
    return bar;
}

try {
    withStrict();
}
catch (error) {
    console.assert(error.name === 'ReferenceError');
}

function withoutStrict() {
    baz = 'baz';
    return baz;
}

console.assert(withoutStrict() === 'baz');

// 3. Strict mode differences
// Silent errors get thrown
function undeletablePropertiesStrict() {
    'use strict';
    delete Object.prototype;  // throws type error in strict
}

try {
    undeletablePropertiesStrict();
}
catch (error) {
    console.assert(error.name === 'TypeError');
}

delete Object.prototype;  // fails silently without strict

// TODO:
// Other differences:
// function dupNames(foo, foo) { return foo; }
// "with" keyword is forbidden
