#!/usr/bin/node
// prints the first argument passed to it

const { argv } = require('process');

if (argv[2]) {
  console.log(argv[2]);
} else if (argv === undefined) {
  console.log('No argument');
}
