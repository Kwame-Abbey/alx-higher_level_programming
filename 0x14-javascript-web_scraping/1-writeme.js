#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');

const filePath = argv[2];
const theString = argv[3];

fs.writeFile(filePath, theString, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
