#!/usr/bin/node
const arr = require('./100-data').list;

const newArr = arr.map(function (element, index) {
  return element * index;
});
console.log(arr);
console.log(newArr);
