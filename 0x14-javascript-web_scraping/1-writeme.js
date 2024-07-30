#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const content = process.argv[3];

if (!filename || !content) {
  console.error('Error: Missing file path or content.');
  process.exit(1);
}

fs.writeFile(filename, content, 'utf8', (error) => {
  if (error) {
    console.error(error);
  }
});
