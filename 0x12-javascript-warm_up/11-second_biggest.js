#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 3) {
  console.log(0);
} else {
  const args = argv.map(Number)
    .slice(2, argv.length)
    .sort((a, b) => b - a);
  console.log(args[1]);
}
