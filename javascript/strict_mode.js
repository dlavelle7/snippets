/*
    Some examples of how 'strict mode' changes normal JavaScript behaviour.
*/

// 1. Strict mode for entire scripts
// Make entire script strict mode by placing literal expression at the
// begining of a script (before any other statements).

// 'use strict';
// foo = 'foo'; // This would cause a Reference error (foo not defined)

// 2. Strict mode for functions
// Put the statement in the functions body before any of its statements
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

// 3. Silent errors get thrown
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
