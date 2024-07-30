#!/usr/bin/node

const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

if (!filePath) {
  console.error('Error: No file path provided.');
  process.exit(1); // Exit the script with a non-zero code to indicate an error
}

// Read the file content
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    // Print the error object if an error occurred
    console.error(err);
  } else {
    // Print the file content
    console.log(data);
  }
});
