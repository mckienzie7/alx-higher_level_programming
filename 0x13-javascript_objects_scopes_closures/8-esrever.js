#!/usr/bin/node
exports.esrever = function (list) {
const arr1 = [];
for(let i = list.length -1; i >= 0; i--){
arr1.push(list[i]);
}
return arr1;
};
