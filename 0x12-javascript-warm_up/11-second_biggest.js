#!/usr/bin/node
function secondBiggest (arr) {
  let max = 0;
  let secondBig = 0;

  for (const val of arr) {
    const num = Number(val);

    if (num > max) {
      secondBig = max;
      max = num;
    } else if (num < max && num > secondBig) {
      secondBig = num;
    }
  }

  return secondBig;
}
const myArray = [];
for (let i = 0; i < process.argv.length - 2; i++) {
  myArray.push(process.argv[i + 2]);
}
console.log(secondBiggest(myArray));
