#!/usr/bin/node
// Substracting the "always here" arguments which are
//   interpreter engine and script path.
const argsNumber = process.argv.length - 2;
// Using a "switch true" to allow writing "conditions" as case
// -> This compares "true" with "result of the boolean expression" so true/false.
switch (true) {
  case argsNumber === 0:
    console.log('No argument');
    break; // Required because JS execute "all other cases" as soon as found one valid.
  case argsNumber === 1:
    console.log('Argument found');
    break;
  case argsNumber > 1:
    console.log('Arguments found');
    break;
}
