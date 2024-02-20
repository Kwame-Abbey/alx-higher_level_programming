#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const filmId = argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request.get({ url: endpoint }, (err, response, data) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(data).characters;

    characters.forEach((character) => {
      const characterUrl = character;
      request.get({ url: characterUrl }, (err, response, data) => {
        if (err) {
          console.error(err);
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(data).name);
        }
      });
    });
  }
});
