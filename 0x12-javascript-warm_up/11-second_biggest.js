#!/usr/bin/node
const arr = process.argv;
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let i;
  for (i = 0; i < process.argv.length; i++) {
    arr[i] = parseInt(process.argv[i]);
  }
  console.log(arr.slice(2).sort(function (a, b) { return b - a; })[1]);
}
