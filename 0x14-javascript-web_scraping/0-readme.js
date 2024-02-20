#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');

const fileName = argv[2];

fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
