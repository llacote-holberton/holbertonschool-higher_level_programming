#!/usr/bin/node

/**
 * Returns the addition of 2 integers.
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
function add (a, b) {
  return a + b;
}

// Several syntax exist.
// Choosing what seems to be the most standard/portable one.
// Exports object, adding an attribute "myattribute", assigning whatever to it.
exports.add = add;
