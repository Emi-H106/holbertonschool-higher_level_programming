#!/usr/bin/node

const arg = process.argv[2];
const count = parseInt(arg);

if (isNaN(count) || count <= 0) {
  if (isNaN(count)) {
    console.log('Missing number of occurrences');
}
} else {
  let i = 0;
  while (i < count) {
    console.log('C is fun');
    i++;
  }
}
