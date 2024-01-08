#!/usr/bin/node
// print x times "C is fun"

const { argv } = require('process');

if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= parseInt(argv[2]); i++) {
    console.log('C is fun');
  }
}
