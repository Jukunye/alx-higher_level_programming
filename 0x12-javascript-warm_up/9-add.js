#!/usr/bin/node
const { argv } = require('process');
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(a, b));
