#!/usr/bin/node
module.exports = class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    let length = '';
    for (let i = 0; i < this.width; i++) {
      length += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(length);
    }
  }
};
