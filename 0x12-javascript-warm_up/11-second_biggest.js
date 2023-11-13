#!/usr/bin/node
const { argv } = require('process');
if (argv.length <= 2) {
    console.log(0);
} else {
    const arguments = argv.slice(2).map(Number).sort((a, b) => b - a)
    console.log(arguments[1]);
}
