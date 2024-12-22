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

## Day 9

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

## Day 10

300/182

Theres hope maybe i dont suck

### Part 1

For each starting position (height=0), run bfs, ensuring you always increase height by exactly 1. If you reach a height=9, add the coord of the 9 to a set. This is the score of the trailhead. Sum all scores.

### Part 2

Same as above, but instead of a set, use a list.

## Day 11

232/407

dp dp dp dp dp dp (wait why are ppl so fast)

### Part 1

fairly standard. on each blink, create a new arrangement according to the rules. iterate over the list and for each element, add the new 1 or 2 stones as described.

### Part 2

75 is too slow to create the entire list (actually the worlds total global flops might actually be enough lol).

First notice stones are independant of other stones, so in the final list, each stone only depends on one initial stone.

We can write a dp function that looks at an individual number and how many blinks are left, and work out how many stones it generates in the final arrangement. e.g. `dp[num][blinks] = num produced stones`

Base case: `dp[num][0] = 1`

Recursive case: what happens on a blink as in part 1
- `dp[0][blinks] = dp[1][blinks-1]`
- `dp[ab][blinks] = dp[a][blinks-1] + dp[b][blinks-1]` where ab is a number with even digits and a, b is the split numbers
- `dp[num][blinks] = dp[num*2024][blinks-1]` otherwise

## Day 12

923/290

wait people thought part 2 was hard paus

### Part 1

use floodfill:

1. have a global visited set starting empty.
3. for each position in the grid, if it isn't in the visited set bfs starting from that element.
   1. put every position you visit into the visited set
   2. keep track of the positions you visited mapped from the starting position `pos_map[starting_pos].append(bfs_cur_pos)`
   3. in the bfs, when you encounter an edge that you don't cross (from out of bounds or from letter is different), add that edge to a separate edges list, mapped from the starting position. the edge can be represented as (position, direction) tuple `edge_map[starting_pos].append((bfs_cur_pos, rejected_direction))`

Note that 2.3. is not part of a standard floodfill.

Now you have the area and perimeter of each region, being the length of the lists of `pos_map` and `edge_map` respectively

### Part 2

In our representation of an edge `(position, direction)`, we can group edges if:

1. They have the same direction
2. They have the same coordinate in the direction perpendicular to direction i.e. `pos.y if dir.y == 0 else pos.x` equal for all `pos` in group
3. the differing position coordinate forms a contiguous array

cba write more, go decipher `calc()` in my code `d12.py` for implementation details

## Day 13

1458/279

yeah i used z3 cuz i forgot there is only one solution lol

### z3

```
# Create an optimizer
opt = z3.Optimize()

# Create variables
a, b = z3.Ints("a b cost")

# Add constraints
opt.add(a*ax + b*bx == targx)
opt.add(a*ay + b*by == targy)

# Add cost calculation
opt.add(cost == ax * 3 + by)

# Minimize cost
m = opt.minimize(cost)

# Extract answer
if opt.check() == z3.sat:
   opt.lower(m)
   ans = opt.model()[cost].as_long()
```

### maths

You can use z3 or numpy linalg, but formally:

Given $x_a, y_a, x_b, y_b, x_{targ}, y_{targ}$, we want to find $a, b$ that satisfies

$$a x_a + b x_b = x_{targ}$$

$$a y_a + b y_b = y_{targ}$$

We can rewrite this simultaneous equations as the matrix equation

$$
\begin{pmatrix}
x_a & x_b\\
y_a & y_b
\end{pmatrix}
\begin{pmatrix}
a\\
b
\end{pmatrix}
=
\begin{pmatrix}
x_{targ}\\
y_{targ}
\end{pmatrix}

$$

Hence:
$$
\begin{pmatrix}
x_a & x_b\\
y_a & y_b
\end{pmatrix} ^ {-1}
\begin{pmatrix}
x_{targ}\\
y_{targ}
\end{pmatrix}
=
\begin{pmatrix}
a\\
b
\end{pmatrix}
$$

The inverse of a 2x2 matrix is given by:

$$\begin{pmatrix}
a & b\\
c & d
\end{pmatrix} ^ {-1} = \frac{1}{ad-bc} \begin{pmatrix}
d & -b\\
-c & a
\end{pmatrix}
$$

We only consider $a, b \in \natnums_0$

## Day 14

379/1271
no way i got out-by-1 in part 2 im so silly

### Part 1

standard. have a list of robot states, containing a tuple of position and velocity. at each timestep, increment position by velocity.

### Part 2

It seems like robots repeat state every 101*103 timesteps. it was sufficient in my case to find the minimum average distance from the centre of the grid `sum((x - xmid)**2 + (y-ymid)**2 for x,y in robotposlist)`.

You may also try minimum average distance from average location of points instead of centre of grid, i.e. `xmid = sum(x for x,y in robotposlist) // len(robotposlist)`

See 2024/d14output.txt for an example expected output.

## Day 15

58/63

i got points omg

### Part 1

moving the robot without boxes is standard, have position tuple `(cx, cy)` and update it with direction `(dx, dy)` based on the direction string, only if the new position isn't `#`

If there is a box in the way `(cx+dx, cy+dy) == "O"`, we need to find the first spot in that direction that is not a box, so will be `#` or `.`. This can be done with a while loop.

If it is `#` then don't do anything. Otherwise, update the grid by:

1. set the empty space after the boxes to `O`
2. move the robot into the first box

i.e. `@OO. -> @OO(O) -> (.@)OO`

### Part 2

After editing the grid, we need to change the box pushing.

For pushing left and right, we can still consider only 1 row as with part 1, but we have to iterate to shift boxes by 1 instead of just adding a box to the end (since boxes have width=2).

Iterating from the back of the box chain, swap the current character with the preceding character, until you reach the front of the box chain.

Pushing up and down can push multiple boxes. The boxes we push form a binary tree, so we can use something similar to tree traversal, with `@` being the root and `[`, `]` being branches.

To check whether it is possible to push the box we have the following function `check()`, which is like checking if there are no `#` in the leaves of our tree:

Base cases:

- `(cx, cy+dy) is '.' -> True`
- `(cx, cy+dy) is '#' -> False`

Recursive cases:

- `(cx, cy+dy) is '[' -> check(cx, cy+dy) and check(cx+1, cy+dy)`
- `(cx, cy+dy) is ']' -> check(cx, cy+dy) and check(cx-1, cy+dy)`

To update boxes assuming it is possible to do so, we need to do 'post order traversal' to move subtrees out of the way before moving the current node:

```
function push(cx, cy, dy){
  if (cx, cy+dy) is '[' {
    push(cx, cy+dy)
    push(cx+1, cy+dy)
  }
  if (cx, cy+dy) is ']' {
    push(cx, cy+dy)
    push(cx-1, cy+dy)
  }

  (cx, cy+dy) = (cx, cy)
  (cx, cy) = '.'  # we want to clear this character since there may not be a box preceding this position
}
```

## Day 16

4327/2760

spent 1hr to find out my comment had east and west swapped. i love my life

### Part 1

Dijkstra's

consider moving forward, turning left and turning right as edges with weights 1, 1000, 1000 respectively, and the state of the reindeer (position and direction) as node.

you can optimise this by only turning if the space ahead after turning is empty, but i don't think this is necessary.

### Part 2

We need to add a dictionary of states to possible previous states. This can be done with a modified version of dijkstra with backtracking.

Make the dijkstra only terminate when all nodes have been visited (don't stop immediately after reached `E`).

We need to be able to visit nodes multiple times, so have a min heap of (score, state) and allow duplicates.

Maintain a dictionary `prev[state] = list of possible previous states`

Instead of updating `prev[next_state] = current state` when adding next state to a priority queue (as with a standard dijkstra), every time you try to add to the min heap, if the distance is equal to the current min distance, append the current state to `prev[state]`. If the distance is strictly less than the current min distance, reset the list to only contain current state.

```
# This the main loop of a minheap variant of dijkstra
score, u = pop min from HEAP
for neighbour v of u
   alt = score + weight from u->v
   if alt < dist[v]:
      add (alt, v) to HEAP
      prev[v] = [u]           # maintain previous path here
   elif alt == dist[v]
      prev[v].append(u)       # and here
```


## Day 17


397/35

Hot take i actually like machine code problems

### Part 1

not much to say other than implement the spec. have a while loop that gets the current opcode and operand based from the instruction pointer. do the operation specified by the opcode as specified by spec.

It is worth noting that adv, bdv and cdv are simply right shifts (`a>>operand`)

### Part 2

bruteforce doesn't work so you have to look at the program. writing it out in pseudocode:

```
do
  b = a%8
  b = b^1
  c = a >> b
  b ^= c
  b ^= 4
  a >>= 3
  print(b%8)
until a==0
```

We can see we are printing `b` after doing some stuff on it, and that `b` depends on only `a`, and that `a` is right shifted by 3 every iteration.

Therefore the last n characters printed only depends on the first (n*3) bits of `a`.

So we can just work backwards to find `a`, generating 3 bits at a time.

Given `a'` that generates `output[n+1:]`, to generate `output[n:]`, we must have `a = a' * 8 + n` where `0<=n<8`.

There may be multiple `n` that generate the same character, so we should consider all possibilities.

## Day 18

178/172

when will i write a template bfs

### Part 1

Standard bfs. would suggest having a set of blocked positions rather than a grid

### Part 2

edit part 1 to be a function returning true if a path exists. binary search on number of bytes to find answer.

## Day 19

285/178

`lru_cache(maxsize=None)` those who know

### Part 1

define function `isPossible(s: string)` which says whether `s` can be made from our base patterns.

Base case: true if `s` is empty string

Recursive case: for each base pattern, if `s` starts with that pattern, remove that pattern from the front of s and check `isPossible(that substring of s)`. If any recursive calls are true, return true, otherwise return false.

### Part 2

define function `count(s: string)` similar to `isPossible`.

Base case: 1 if `s` is empty string

Recursive case: sum of all `count(substring)` for each substring made by removing a base pattern from the front. this should be 0 if no substrings can be made.

use memoization.

## Day 20

1096/523

idk why i thought my O(n^6) solution would be fast enough

### Part 1

First, precompute shortest distances from every point from the start, and same from the end by bfs.

Next iterate through every wall in the grid. if it is possible to skip through the wall (i.e. `.#.` or the vertical one), the time taken using this cheat would be `distance_from_start[point before cheat] + distance_from_end[point after cheat] + 2`. Notice you can go through each cheat forwards and backwards (i.e. `S#E` (->) and `E#S` (<-)). Sum all the cheats that save >=100 time.

### Part 2

Each cheat is just a pair of positions that have taxicab distance of <=20.

We bruteforce by iterating over all pairs of points that:

- are both not walls (not `#`)
- have taxicab distance less than 20

and work out the time taken as above: `distance_from_start[cheat_start] + distance_from_end[cheat_end] + taxicab_distance(cheat_start, cheat_end)`

As an optimization, notice given the first point `(sx, sy)`, the bounds of the second point `(ex, ey)` are

```
ex = [sx-20, sx+20]
ey = [sy-20 + |sx-ex|, sy+20 - |sx-ex|]
```

(by taxicab distance constraint)

## Day 21

1275/735

brain too small for this

### Part 1

we will call the robot being controlled a level up from the robot controlling.

first precompute the inputs required to go from two points for both keypads. Assume that the shortest path is optimal for example:

- to move from `A -> 2`, we can have `^<A` or `<^A`
- to move from `A -> <`, we can have `<v<A` or `v<<A`

define a function that computes the following: given a sequence of inputs and the number of levels to go up, calculate the number of inputs required to generate the sequence of inputs.

We will implicitly add an `A` to the start of the string, since every sequence must both start and end on `A`

recurse(string, level)

Base case:

- `if level == 0: return len(string)`

Recursive case: find the minimum chars required to generate our string from the level up, using our precomputed list of possible chars and recursing.

```
total_chars = 0
for (start, end) in transition defined by string:
   paths: list[str] = precomputed paths from start to end
   total_chars += min(recurse(path, level-1)) for all paths
return total_chars
```

### Part 2

memoize the recursive function

## Day 22

125/601

i didnt see the sequence was 4 long lol.

### Part 1

just implement the algorithm described. worth noting you can use bit shifts instead of multiplies, but there is negligible difference.

### Part 2

create difference arrays (`arr[i+1]-arr[i]`) corresponding to price arrays from our part 1 generator for each monkey.

have a global counter mapping from array of 4 consecutive differences to bananas gained.

for each monkey, in the difference array, for each consecutive 4 differences, if it was the first time we've seen this subarray, then add it to the global counter, mapping to the corresponding gained bananas.

get the maximum gained bananas from our counter.