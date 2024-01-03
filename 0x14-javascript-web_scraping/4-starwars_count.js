#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const filmsArray = JSON.parse(body).results;
  const actorName = 'https://swapi-api.alx-tools.com/api/people/18/';
  let count = 0;

  filmsArray.forEach(key => key.characters.includes(actorName) ? count++ : null);
  console.log(count);
});
