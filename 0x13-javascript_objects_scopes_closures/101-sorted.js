#!/usr/bin/node
const dict = require('./101-data').dict;
const newdict = {};
for (const key in dict) {
  const value = dict[key];
  if (newdict[value] === undefined) {
    newdict[value] = [key];
  } else {
    newdict[value].push(key);
  }
}
console.log(newdict);
