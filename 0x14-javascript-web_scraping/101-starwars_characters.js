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
    const charactersCount = characters.length;
    let completedRequests = 0;

    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (!error) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
        completedRequests++;

        // Check if all requests are done before continuing
        if (completedRequests === charactersCount) {
          // All requests done
        }
      });
    });
  } catch (e) {
    console.error('Error parsing JSON:', e);
  }
});
