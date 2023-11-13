#!/usr/bin/node
const myVar = process.argv.length;
if (myVar === 1){
console.log('Not a number');
}
else{
if (isNaN(process.argv[2])){
console.log('Not a number');
}
else{
console.log('My number: '+process.argv[2]);
}}
