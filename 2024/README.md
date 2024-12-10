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

## Day 5

705/435

Interesting today, theres definitely a graph theory approach (DAGs) but i cba think about it.

### Part 1

we can build a dependency dictionary as follows: `d[x]` is a list of `y`s where `y` must be before `x`.

For each update, we can iterate over `update[i]` and check that none of `update[i:]` is in the dependency list of `update[i]`. If so, it is valid.

### Part 2

Use same algo as part 1 to find invalid updates. When we fail the condition `none of update[i:] in d[update[i]]`, for each dependency in `update[i:]`, move that element to the front of the update. Do this in a while loop until the update is valid.

## Day 6

617/440

Im starting to not like grids, and i have a feeling this year will be grid heavy...

### Part 1

Fairly standard question. Have a position `(x, y)` and direction `(dx, dy)`, and each timestep, do position + direction `(x+dx, y+dy)`. If you hit a `#` then rotate by changing direction tuple. This is easiest done with a list of directions. Shove visited positions into a set to count without duplicates.

### Part 2

I thought about doing it properly, then thought "what if i could bruteforce it" lol.

Turns out, setting each square in the grid to `#`, then running algorithm in part 1, but exiting when you get in a loop, and counting how many times you loop works in ~1min. im honestly impressed.

I think to do it properly, you need to look at consecutive turning points and check if the 4th turning point to make a square would be blocked by another `#` or something. Im too tired to work it out tho.

## Day 7

770/1259

The reverse of left-to-right is indeed right-to-left. good job brain

### Part 1

have a recursive function `func` that tells us if an array `g` can have result `ans`.

Base case, if `g` is empty, true if `ans==0`, false otherwise

Recursive cases:

- `func(g[:-1], ans/g[-1])` if `ans` divisible by `g[-1]` (multiplication case)
- `func(g[:-1], ans-g[-1])` if `ans > g[-1]` (addition case)

Basically for each operation try to undo it from the answer if possible

### Part 2

Just add an extra case to our recursive part:

- truncate off the last digits of `ans` if the last digits are the same as `g[-1]`

## Day 8

898/479

I hate corner cases

### Part 1

Get pairs of antennas with same frequency. you can do this by having a map of frequency to positions and have a nested for loop.

Let the two positions of antennas be `a` and `b`.
The antinodes are at `a + (a-b)` and `b - (a-b)`.

### Part 2

Get pairs of antenna as above `a`, `b`.

Now repeatedly add `a-b` to `a`, and repeatedly subtract `a-b` to `b` until they go out of bounds.

## Part 9

426/4489.

The classic do it the same way 3 times and get 3 different answers.

### Part 1

We know the length of the resulting file system will be the number of file blocks (`sum(l[::2])`). Call this length `len`

Create an array `arr` of length `len` representing the memory. Add file IDs to the array with gaps by maintaining an index into `arr` (e.g. `0..111..`) Once the array is full, add remaining blocks into a list.

Then iterating on the list in reverse order, fill in the gaps.

### Part 2

Create a list of tuples `(fileID, length of block)` and give free blocks `fileID=-1`.

Iterate backwards over the list, trying to move used blocks to the front of this list. This can be done as follows:

- Iterate backwards over the list, skipping free blocks
- At each used block `(back_id, back_size)`, find the first free block from the start of the list `(-1, front_size)` where `front_size>=back_size`, ensuring the free block is before the used block.
- shrink the free block and move the used block to before our free block.

You can optimise this a bit by removing the free block if it shrinks to 0 size.

## Part 10

300/182

Theres hope maybe i dont suck

### Part 1

For each starting position (height=0), run bfs, ensuring you always increase height by exactly 1. If you reach a height=9, add the coord of the 9 to a set. This is the score of the trailhead. Sum all scores.

### Part 2

Same as above, but instead of a set, use a list.