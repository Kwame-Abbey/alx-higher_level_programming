#!/usr/bin/node
// prints a message depending of the number of arguments passed

const { argv } = require('process');

const argsCount = argv.length - 2;

if (argsCount <= 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
