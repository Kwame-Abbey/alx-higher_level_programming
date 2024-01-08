#!/usr/bin/node
// Prints two arguments passed to it

const { argv } = require('process');

const firstArgument = argv[2];
const secondArgument = argv[3];

console.log(firstArgument + ' ' + 'is' + ' ' + secondArgument);
