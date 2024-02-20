#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const done = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const current = tasks[i];
      if (current.completed === true) {
        if (done[current.userId] === undefined) {
          done[current.userId] = 1;
        } else {
          done[current.userId]++;
        }
      }
    }
    console.log(done);
  }
});
