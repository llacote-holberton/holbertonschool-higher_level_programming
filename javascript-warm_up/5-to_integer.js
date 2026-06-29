#!/usr/bin/node
const firstArgAsNumber = Number(process.argv[2]);
if (isNaN(firstArgAsNumber)) console.log('Not a number');
else console.log('My number: ' + firstArgAsNumber);
