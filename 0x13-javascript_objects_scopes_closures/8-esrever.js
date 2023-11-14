#!/usr/bin/node
exports.esrever = function (list) {
  const revArr = [];
  let j = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    revArr[i] = list[j];
    j--;
  }
  return revArr;
};
