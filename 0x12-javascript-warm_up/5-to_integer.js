#!/usr/bin/node
const { argv } = require('process');
const integer = parseInt(argv[2]);

if (isNaN(integer)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + integer);
}
