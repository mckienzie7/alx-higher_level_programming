#!/usr/bin/node
const count = process.argv[2];

if (count === 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
