#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');
const request = require('request');

const endpoint = argv[2];
const filePath = argv[3];
let theString;

request.get({ url: endpoint }, (err, response, data) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    theString = data;
  }
  fs.writeFile(filePath, theString, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
