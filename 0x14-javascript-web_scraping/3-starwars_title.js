#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const movieID = argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get({ url: endpoint }, (error, response, data) => {
  if (error) {
    console.error(error);
  }
  if (response.statusCode === 200) {
    console.log(JSON.parse(data).title);
  }
});
