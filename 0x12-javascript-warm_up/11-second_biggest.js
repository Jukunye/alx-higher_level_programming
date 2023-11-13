#!/usr/bin/node
const { argv } = require('process');
let biggest = 0;
let second = 0;

for (let i = 2; i < argv.length; i++) {
  if (parseInt(argv[i]) > biggest) {
    second = biggest;
    biggest = parseInt(argv[i]);
  }
}

console.log(second);
