#!/usr/bin/node
const mySize = parseInt(process.argv[2]);

if (mySize === 0 || isNaN(mySize) === true) {
  console.log('Missing size');
} else {
  let num = '';
  for (let i = 0; i < mySize; i++) {
    num += 'X';
  }
  for (let j = 0; j < mySize; j++) {
    console.log(num);
  }
}
