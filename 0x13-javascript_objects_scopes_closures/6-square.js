#!/usr/bin/node

const Sq = require('./5-square');
module.exports = class Square extends Sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let length = '';
      for (let i = 0; i < this.width; i++) {
        length += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(length);
      }
    }
  }
};
