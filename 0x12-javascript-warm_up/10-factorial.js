#!/usr/bin/node
const { argv } = require('process');
const n = parseInt(argv[2]);

function fuctorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * fuctorial(n - 1);
  }
}

console.log(fuctorial(n));
