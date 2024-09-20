#!/usr/bin/node
const request = require('request');

// Retrieve the movie ID from command-line arguments
const movieId = process.argv[2];

// Construct the API URL for the specific movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch character names recursively
function fetchCharacter (idx, characters) {
  if (idx === characters.length) {
    return; // Stop when all characters have been printed
  }

  request(characters[idx], function (error, response, body) {
    if (!error) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);

      // Recursive call to fetch the next character
      fetchCharacter(idx + 1, characters);
    } else {
      console.error('Error fetching character:', error);
    }
  });
}

// Make an API request to get the movie data
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Start fetching the characters one by one, in order
    fetchCharacter(0, characters);
  }
});
