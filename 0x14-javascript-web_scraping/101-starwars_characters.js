#!/usr/bin/node
const request = require('request');

function findName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
  async (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const data = JSON.parse(body);

    for await (const character of data.characters) {
      try {
        const name = await findName(character); // Use await here
        console.log(name);
      } catch (error) {
        console.log(error);
      }
    }
  });
