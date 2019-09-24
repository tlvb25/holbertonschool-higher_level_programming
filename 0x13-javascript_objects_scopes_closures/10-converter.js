#!/usr/bin/node

exports.converter = function (base) {
    function num_converter (n) {
      return n.toString(base);
    }
    return num_converter;
  };
