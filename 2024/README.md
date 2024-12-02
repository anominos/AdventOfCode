# Advent of code 2024

Here we go again

## Day 1

Template code OP.

### Part 1
<details>

zip returns iterator of pairs, generated from 2 sequences. zip is good.

</details>

### Part 2
<details>

good old collections.Counter

</details>

## Day 2

A bit of minor DDOS (totally me not coping at being bad)

### Part 1

np.diff returns an array of `x[i+1] - x[i]`s, so the second condition is a min/max
first condition is when the diff array is all positive or all negative.

### Part 2

simple brute force, `for i in range(len(arr)): arr[:i] + arr[i+1:]` will remove i-th element from the array.