#!/usr/bin/node

// We only want the first "real" argument so we don't care whether there are
//   or not "more arguments than one"
// "Using length is forbidden" per task requirement
// if process.argv.length >= 3 console.log(process.argv[2]);
const firstArg = process.argv[2];
if (firstArg !== undefined) console.log(firstArg);
else console.log('No argument');

// ===== DRAFT =====
// First version: NOT OPTIMAL AT ALL
// Because our "business need" only cares about the FIRST argument
//   and by definition it will always be index 2 of the arguments array.
// const argsTotalLength = process.argv.length;
// There is always two "starting arguments" which are
//   interpreter engine and script path so we must require at least 3 arguments.
// if (argsNumber < 3)  console.log('No argument');
// else console.log(process.argv[2])
