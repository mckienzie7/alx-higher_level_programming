#!/usr/bin/node
exports.callMeMoby = function (num, theFunc) {
  for (let i = 0; i < num; i++) {
    theFunc();
  }
};
