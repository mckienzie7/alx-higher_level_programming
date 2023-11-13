#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
const C = 'C is fun';
if (isNaN(myNum) === true) {
  console.log('Missing number of occurrences');
} else {
	for (let i = 0; i < myNum; i++){
		console.log(C);
}
}
