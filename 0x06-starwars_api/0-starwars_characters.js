#!/usr/bin/node
const request = require('request');

// Retrieve the movie ID from command-line arguments
const movieId = process.argv[2];

// Construct the API URL for the specific movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch character names asynchronously
function fetchCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error) {
        const characterData = JSON.parse(body);
        resolve(characterData.name); // Resolve with character name
      } else {
        reject(error); // Reject if there's an error
      }
    });
  });
}

// Make an API request to get the movie data
request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Use Promise.all to fetch all character names concurrently
    try {
      const characterNames = await Promise.all(
        characters.map((url) => fetchCharacter(url))
      );

      // Print characters in order after all requests complete
      characterNames.forEach((name) => console.log(name));
    } catch (err) {
      console.error('Error fetching characters:', err);
    }
  }
});
