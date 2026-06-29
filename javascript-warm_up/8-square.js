#!/usr/bin/node
// By design first argument must be the square size (note: JS will "upper-round" a float whatever happens).
const squareSize = Number(process.argv[2]);

if (isNaN(squareSize)) console.log('Missing size');
else for (let i = 0; i < squareSize; i++) console.log('X'.repeat(squareSize));

/* ===== Task instructions ====
 * Write a script that prints a square
 * The first argument is the size of the square
 * If the first argument can't be converted to an integer, print "Missing size"
 * You must use the character X to print the square
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 * You must use a loop (while, for, etc.)
 */
