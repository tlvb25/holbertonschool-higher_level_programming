#!/usr/bin/node

const list = require('./100-data').list;
console.log(list);

const new_list = list.map((v, i) => v * i);
console.log(new_list);
