#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (NaN(x)) {
  console.log('Missing number of occurrences')
} else {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
