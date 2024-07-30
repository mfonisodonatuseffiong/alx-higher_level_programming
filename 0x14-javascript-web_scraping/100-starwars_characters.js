#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (!error) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  } catch (e) {
    console.error('Error parsing JSON:', e);
  }
});
