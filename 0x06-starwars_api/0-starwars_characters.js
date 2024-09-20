#!/usr/bin/node
// Import the request module to make HTTP requests
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL for the specific movie using the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a request to the Star Wars API to get movie details
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the response body into JSON
  const movieData = JSON.parse(body);

  // Retrieve the character URLs from the movie data
  const characterUrls = movieData.characters;

  // Function to fetch each character's name
  function fetchCharacterName (url) {
    request(url, function (error, response, body) {
      if (error) {
        console.error('Error:', error);
        return;
      }
      // Parse the character data and print the name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }

  // Loop through the character URLs and fetch each character's name
  characterUrls.forEach((url) => fetchCharacterName(url));
});
