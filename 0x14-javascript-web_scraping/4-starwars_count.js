#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Error: API URL argument is required');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    let movieCount = 0;

    // Check each movie for character ID 18
    data.results.forEach((movie) => {
      if (movie.characters.some(character => character.includes('18'))) {
        movieCount++;
      }
    });

    console.log(movieCount);
  } else {
    console.error('Error: Failed to retrieve data');
  }
});
