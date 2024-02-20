#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const endpoint = argv[2];

request.get({ url: endpoint }).on('response', (response) => {
  console.log(`code: ${response.statusCode}`);
});
