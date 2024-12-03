# Advent of code 2024

Here we go again

## Day 1

33/39

Template code OP.

### Part 1

zip returns iterator of pairs, generated from 2 sequences. zip is good.

### Part 2

good old collections.Counter

## Day 2

819/851

A bit of minor DDOS (totally me not coping at being bad)

### Part 1

np.diff returns an array of `x[i+1] - x[i]`s, so the second condition is a min/max
first condition is when the diff array is all positive or all negative.

### Part 2

simple brute force, `for i in range(len(arr)): arr[:i] + arr[i+1:]` will remove i-th element from the array.

## Day 3

770/490

String processing sucks

### Part 1

just use a regex. `\d+` will match all numbers.

### Part 2

my approach is just to overbracket a regex, then use `in` or random indices to get the relevent parts lol.