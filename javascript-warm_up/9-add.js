#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
if (!Number.isInteger(num1) || !Number.isInteger(num2)) console.log('NaN');
else console.log(add(num1, num2));

/* ===== Task instructions ====
 * Write a script which defines and uses a function to print the addition of two integer arguments
 * The first argument is the size of the square
 * If the first argument can't be converted to an integer, print "Missing size"
 * You must use the character X to print the square
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 * You must use a loop (while, for, etc.)
 */
