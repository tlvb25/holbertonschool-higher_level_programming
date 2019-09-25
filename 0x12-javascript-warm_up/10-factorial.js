#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === 1 || n === 0) {
    return 1;
  } else {
    return factorial(n - 1) * n;
  }
}
const num = parseInt(process.argv[2]);
console.log(factorial(num));
