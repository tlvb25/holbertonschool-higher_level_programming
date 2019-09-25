#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (NaN(x)) {
  console.log('Missing number of occurrences')
} else {
  console.log('C is fun\n'.repeat(x))
}
