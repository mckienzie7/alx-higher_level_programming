#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
const n  = list.length;
let x = 0;
for (let i = 0; i < n; i++){
  if (list[i] == searchElement) {
    x+=1;
  }
}
return x;
}  
