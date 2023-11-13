#!/usr/bin/node
exports.addMeMaybe = function (num, theFunc) {
  const number = num + 1;
  theFunc(number);
};
