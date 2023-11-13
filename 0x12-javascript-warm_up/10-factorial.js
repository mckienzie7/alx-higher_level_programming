#!/usr/bin/node
const myNum = parseInt(process.argv[2]);

function factorial (num) {
  if (isNaN(num) === true || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const myFact = factorial(myNum);
console.log(myFact);
