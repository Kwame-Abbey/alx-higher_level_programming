#!/usr/bin/node
// prints a message depending of the number of arguments passed

const { argv } = require('node:process');

const argsCount = argv.length;

if (argsCount === 2) {
  console.log('No argument');
} else if (argsCount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
