#!/usr/bin/node
const request = require('request');

// Retrieve the movie ID from command-line arguments
const movieId = process.argv[2];

// Construct the API URL for the specific movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch character data sequentially
function fetchCharactersSequentially (characters, idx = 0) {
  if (idx >= characters.length) {
    return; // Stop when all characters are processed
  }

  // Make request for the current character
  request(characters[idx], (error, response, body) => {
    if (!error) {
      const characterData = JSON.parse(body);
      console.log(characterData.name); // Print character name
      // Move to the next character
      fetchCharactersSequentially(characters, idx + 1);
    } else {
      console.error('Error:', error);
    }
  });
}

// Make an API request to get the movie data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Start fetching character data sequentially
    fetchCharactersSequentially(characters);
  }
});
