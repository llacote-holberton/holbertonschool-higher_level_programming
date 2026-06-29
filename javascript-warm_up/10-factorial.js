#!/usr/bin/node

function getFactorial (n) {
  if (n === 1) return 1;
  else return n * getFactorial(n - 1);
}

const factorialNumber = Number(process.argv[2]);
if (isNaN(factorialNumber) || factorialNumber < 2) console.log(1);
else console.log(getFactorial(factorialNumber));

/* ===== Task instructions ====
 * Write a script that computes and prints a factorial, with first argument to be
 *   cast as integer to indicate the factorial to compute.
 * Factorial of NaN is 1.
 * You must do it by using a recursive function.
 */
