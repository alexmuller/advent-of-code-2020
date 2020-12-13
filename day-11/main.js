const fs = require('fs').promises;
const part1 = require('./lib/part-1');


const filename = process.argv[2];

fs.readFile(filename, 'utf-8').then(contents => {
    console.log(`Part 1: ${part1(contents)}`);
})
