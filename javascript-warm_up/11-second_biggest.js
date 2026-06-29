#!/usr/bin/node

// NOTE: can be chained because slice is an Array method which returns an Array,
//   and map is also an Array method which returns an Array.
// .map(Number) is short-hand syntax of .map(element => Number(element))
//    which creates a new array, parsing each element of original one and converting is as Number
//    before affecting it as an element of the new array.
const numberArguments = process.argv.slice(2).map(Number);

// Since I must define a sorting method AND it would be annoying to use array.length - 2
//   might as well directly sort in optimal order so I know my target item is at index 1.
function sortNumbersInDescendingOrder (a, b) { return b - a; }

// Using intermediate Set back and forth conversion to remove duplicates.
const finalArray = Array.from(new Set(numberArguments)).sort(sortNumbersInDescendingOrder);
console.log(finalArray[1]);

/* ===== Task instructions ====
 * Write a script that searches the second biggest integer in the list of arguments.
 * You can assume all arguments can be converted to integer
 * If no argument or only 1 passed, print 0
 */

/* ===== BRAINSTORM / EXPLORATION =====
 * === EXTRACTING "part of an array" and converting its items ===
 * I saw all these different methods to "get an array of arguments as Integers"
 * a) Putting aside the non-pertinent elements of process.argv (0, 1) by using...
 *    - either "destructuring" with '...rest' syntax (const [, , ...arguments] = process.argv)
 *      => Modern and efficient as it does not affects the original array
 *    - or removing manually with two array.shift() on a copy of process.argv ("extracts" the FIRST element).
 *      => WORST method since making a copy PLUS .shift() forces Javascript to reindex the remaining elements.
 *    THEN converting the items in resulting array as Numbers.
 * b) Using .filter to remove "non-convertible elements" then .map to make a "processed copy" of argv.
 *    => Complex and could theorically have unintended behaviour in case script name is actually readable as a number.
 *
 * => Best method is using slice(2) which is exactly designed to create a subset of array, and therefore the fastest.
 * => AND chain it with just a .map is enough BECAUSE task "guarantees" all given arguments are convertable
 *    (otherwise we would need to chain with a .filter(element => !isNaN(element))),
 *    or even stricter !Number.isInteger(element)).
 *
 * === FINDING THE 2nd HIGHEST ===
 * I see two methods: using the Maths module or just sorting our array and using indexes.
 * IMO sorting is by far the most simple and quickest, and I don't see any edge case where it would have
 *   unintended behaviour.
 *
 *
 * === DRAFT ===
 * // Annoying way to do because require extra work.
 * Note: among all other crazyness of Javascript sort() is ABSOLUTELY USELESS BY DEFAULT.
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort
 * function sortNumbers (a, b) { return a - b }
 * finalArray = Array.from(new Set(numberArguments)).sort(sortNumbers);
 * console.log(finalArray.at(-1)); REQUIRES MODERN Javascript (for Node, v16+)
 * console.log(finalArray(finalArray.length -2))
 */
