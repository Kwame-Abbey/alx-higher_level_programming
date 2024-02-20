#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const endpoint = argv[2];

request.get({ url: endpoint }, (err, response, data) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const filmsList = JSON.parse(data).results;
    let filmCount = 0;

    filmsList.forEach((film) => {
      const characters = film.characters;
      characters.forEach((character) => {
        if (character.includes('18')) {
          filmCount++;
        }
      });
    });
    console.log(filmCount);
  }
});
