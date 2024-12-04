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

## Day 4

1874/805

Edge case hunter (i didnt know/have any grid librarys)

edit: idk why i didn't iterate over all diagonal dirs for part 1 lol

### Part 1

We can do left/right by iterating over indices and checking `l[i][j:j+4]` is either `XMAS` or `SAMX`

We can do up/down by rotating the list `list(zip(*l[::-1]))` and doing the same as left/right

For diagonals, for each index, go in a diagonal direction, add to list and check it is `XMAS`.

### Part 2

Iterate over indices. Check the 4 diagonally adjacent elements have 2 `M`s and 2 `S`s. Also need to check the diagonals aren't the same, so we don't have:
```
M.S
.A.
S.M
```
