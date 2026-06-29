#!/usr/bin/node
// By design we require first argument to be the number of repetitions.
const repetitionsNumber = Number(process.argv[2]);
// Fun fact: if input provided would be read as a float, JS rounds it "upperward"
//   instead of rounding mathematically (ex 6.242 -> 7 times)

if (isNaN(repetitionsNumber)) console.log('Missing number of occurrences');
else for (let i = 0; i < repetitionsNumber; i++) console.log('C is fun');
