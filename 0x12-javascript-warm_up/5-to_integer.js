#!/usr/bin/node
const myNum = parseInt(process.argv[2]);

if (isNaN(myNum) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNum);
}
