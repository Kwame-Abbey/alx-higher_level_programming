#!/usr/bin/node

const { argv } = require("node:process");
const request = require("request");

const filmId = argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request.get({ url: endpoint }, (err, response, data) => {
  if (err) {
    console.error(err);
    return;
  } else if (response.statusCode === 200) {
    let charDict = {};
    const characters = JSON.parse(data).characters;

    characters.forEach((character) => {
      let characterUrl = character;
      request.get({ url: characterUrl }, (err, response, data) => {
        if (err) {
          console.error(err);
          return;
        } else if (response.statusCode === 200) {
          charDict[character] = JSON.parse(data).name;
        }

        if (characters.length === Object.keys(charDict).length) {
          for (let key in charDict) {
            console.log(charDict[key]);
          }
        }
      });
    });
  }
});

