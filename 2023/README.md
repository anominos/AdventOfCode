# Advent of code 2023

Another year of massacring my sleep schedule

- [Advent of code 2023](#advent-of-code-2023)
  - [Day 1](#day-1)
    - [Part 1](#part-1)
    - [Part 2](#part-2)
  - [Day 2](#day-2)
    - [Part 1](#part-1-1)
    - [Part 2](#part-2-1)
  - [Day 3](#day-3)
    - [Part 1](#part-1-2)
    - [Part 2](#part-2-2)
  - [Day 4](#day-4)
    - [Part 1](#part-1-3)
    - [Part 2](#part-2-3)
  - [Day 5](#day-5)
    - [Part 1](#part-1-4)
    - [Part 2](#part-2-4)
  - [Day 6](#day-6)
    - [Part 1](#part-1-5)
    - [Part 2](#part-2-5)
  - [Day 7](#day-7)
    - [Part 1](#part-1-6)
    - [Part 2](#part-2-6)
  - [Day 8](#day-8)
    - [Part 1](#part-1-7)
    - [Part 2](#part-2-7)
  - [Day 9](#day-9)
    - [Part 1](#part-1-8)
    - [Part 2](#part-2-8)
  - [Day 10](#day-10)
    - [Part 1](#part-1-9)
    - [Part 2](#part-2-9)
  - [Day 11](#day-11)
    - [Part 1](#part-1-10)
    - [Part 2](#part-2-10)
  - [Day 12](#day-12)
    - [Part 1](#part-1-11)
    - [Part 2](#part-2-11)
  - [Day 13](#day-13)
    - [Part 1](#part-1-12)
    - [Part 2](#part-2-12)
  - [Day 14](#day-14)
    - [Part 1](#part-1-13)
    - [Part 2](#part-2-13)
  - [Day 15](#day-15)
    - [Part 1](#part-1-14)
    - [Part 2](#part-2-14)
  - [Day 16](#day-16)
    - [Part 1](#part-1-15)
    - [Part 2](#part-2-15)
  - [Day 17](#day-17)
    - [Part 1](#part-1-16)
    - [Part 2](#part-2-16)
  - [Day 18](#day-18)
    - [Part 1](#part-1-17)
    - [Part 2](#part-2-17)
  - [Day 19](#day-19)
    - [Part 1](#part-1-18)
    - [Part 2](#part-2-18)
  - [Day 20](#day-20)
    - [Part 1](#part-1-19)
    - [Part 2](#part-2-19)


## Day 1

### Part 1
<details>

Part 1 is fairly standard. Just need to edit my template code from extracting all numbers to all digits with `r"-?\d"` instead.

</details>

### Part 2

<details>

For part 2, observe that you can just replace each copy of each number in words with word + digit + word (e.g. replace `"one"`  with `"one1one"`). Then you can do the same as part 1.

</details>

## Day 2

No not the text formatting :(

### Part 1

<details>

Went for the classic chain of `.split()`s.

Looking back, probably should have had 3 regexes, one for reds one for blues and one for greens, to get a list for each colour.

</details>

### Part 2

<details>

Used a defaultdict and take the `max(mydict[colour], new_val_for_colour)`.

</details>


## Day 3

Forgot to update duplicated code outside of loop :(.

### Part 1

<details>

Iterate over each character of each line, and append to current number if current character is a digit. If current character is not a digit, check for adjacent symbol and then reset the current number.

To check for adjacent symbol, at each digit, check the 8 adjacent squares for a square that is not '.' or a digit, and store a boolean that is True when any digit is adjacent to a symbol.

</details>

### Part 2

<details>

Store a dictionary of key=(coord of gear), value=(all adjacent part numbers as list)

When checking for symbol, if any adjacent symbol is '*', add part number to dictionary.

At end, iterate over dictionary and add gear ratio if exactly 2 part numbers are adjacent to the gear (length of list == 2).

</details>

## Day 4

Accidentally read the card number as part of the first list :P.

### Part 1

<details>

Use set union on the two lists, and add `2**length of union`. Remember to check the edge case where the length is 0.

</details>

### Part 2

<details>

Store a running counter of number of cards.

When updating the counter, you can increment the range `[i+1, i+(number of winners)]` by `counter[i]` where `i` is the current card number.

</details>

## Day 5

Already starting to get tough? Oh dear.

### Part 1

<details>

Thankfully, the mappings are already in order which they need to be applied

For each map:

Iterate over your current seed (or whatever)

Iterate over each range in the mappings and check if your current seed is within that range.

If it is, scale that seed to the new range.

</details>

### Part 2

<details>

The idea is to split each range into three for every mapping range, the bit before the mapping range, the bit inside the mapping range and the bit after the mapping range.

For each mapping:

iterate over the ranges in source range start order.

for each range of seeds, if it intersects with the current mapping range:

1) split into the three ranges described above (I will refer to them as pre, in and post)
2) since this is the first range we encountered that intersects, we know that the pre-range does not correspond to any mapping, so add the pre-range to the next list unchanged.
3) scale the in-range
4) recursively apply this algorithm to the post-range, until the post-range does not intersect with any ranges, then you can add the remaining range unchanged.

</details>

## Day 6

Can't write binary search properly smh.

### Part 1

<details>

The times are small enough to iterate through all possible lengths to hold the button.

The formula for getting the distance travelled is `(total_time - time_held) * time_held`

</details>

### Part 2

<details>

Observe that the distance travelled increases the longer you hold the button until `time_held = total_time//2` (or something similar with odd numbers), and that the distance travelled is symmetrical around that point.

Binary search on half the `total_time` for the point where you start winning. You can then calculate the total number of winning states by mirroring the calculated value.

NB: not sure if my code works on even times.

Edit: Just realised that inputs are actually small, so you can still use part 1 for this XD.

</details>

## Day 7

5 Aces, ok.

### Part 1

<details>

Use python's built in sort with a custom key.

Key can return a lower number for better types of hand and a higher number for a worse type of hand, e.g. 0 for 5 of a kind, 1 for 4 of a kind etc.

NB you can do it the other way round i.e. higher number for better hand, but be careful to match the second part of the key (may need to reverse list of card strengths)

You can then add on a tuple to the end of the key for the second ordering rule (by getting index of each card in the list of cards sorted by strength, and having a tuple of indices)

There are many ways to get the type of card. I used a combination of `len(set())` and `collections.Counter`, e.g. `len(set(a)) == 1` -> 5 of kind. The exact logic is left as an exercise to the reader (or by looking at the code).

</details>

### Part 2

<details>

First notice that having the `J`s map to the same card is always better than having them map to different cards.

Iterate over all possible other cards, replace all `J`s with that card and check the resulting type of hand (using part 1). Then take the best type and use that as the type key instead.

</details>

## Day 8

Noooo I thought it was a search XD.

### Part 1

<details>

Start from `AAA`, and iterate through your instruction string until you reach `ZZZ`. I used a dictionary of 2-tuples to store the tree.

</details>

### Part 2

<details>

Do part 1 on all nodes ending with `A` until they reach a node ending `Z`, to get a list of lengths.

The solution is the lcm of all the numbers. To calculate this, find lcm of each term incrementally, i.e. `reduce(lcm, my_list_of_lengths, 1)`.

</details>

## Day 9

### Part 1

<details>

Use recursion to get the next value for each next value for each level of difference.

The base case is when all numbers are equal, then return the number. (You can do when they are all 0 as well).

Otherwise, find the 'next difference' and return the last value in your current list to this next difference.

The difference array can be calculated with `np.diff`.

</details>

### Part 2

<details>

Do part 1, but subtrace the 'next difference' from the first value instead.

</details>

## Day 10

Difficulty of problem is directly proportional to the amount of code commented out.

My implementation is awful but I cba fix it.

### Part 1

<details>

First determine which pipe type "S" is, by checking adjacent pipes or otherwise.

Then loop around the whole loop. You can either go both ways until they meet and count the steps taken, or go around one way and divide the total length by two.

</details>

### Part 2

<details>

It is sufficient to check if there is an odd number of vertical pipes to the left of the current square if the square is inside the loop. ([See Ray Casting Algorithm for point-in-polygon detection](https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm))

E.g. Consider `|a|b|c|`, `a` and `c` have 1 and 3 vertical pipes to the left of them respectively so are inside the loop. `b` has 2 pipes to the left so is not in the loop. Note `a, b, c` are not limited to single characters, and this fact works for any loop.

For the case of corners, we can treat `F--J` and `L--7` as single walls, and `F--7` and `L--J` as double walls. (Note arbitrary number of `-`s)

</details>

## Day 11

### Part 1

<details>

Decided to actually add all the new rows and columns.

Check if rows are empty, and double it if so. (Use `not any()`)

Rotate the list 90 degrees, and repeat the duplicating of rows.

Then rotate the list 90 degrees three more times.

Getting distance between all pairs can be done by `abs(x1-x2) + abs(y1-y2)`, remembering not to count each pair twice.

</details>

### Part 2

<details>

Instead of adding rows, instead store the index of empty rows and columns.

When adding the coordinate of each galaxy to find distances, instead add the number of empty columns/rows preceding the current galaxy, and multiply by `999,999`.

</details>


## Day 12

AintNoWay I cheesed part 2 XD.

### Part 1

<details>

Use a recursive function to bruteforce all possibilities, pruning out invalid cases early.

The inputs to the recursive function should be the current string to consider, the remaining list of groups. The function should return the number of rearrangements for the inputs. (It may be helpful to also input whether the previous character was a `.`)

If the first character is `?`, replace it with both `#` and `.`, and sum the counts of each case. For when the first character is `.` or `#`, update the remaining list of groups appropriately and recurse on `current_string[1:]`.

You can prune when e.g. You have a negative group (i.e. too many `#`s in a row), or when you have too many groups.

</details>

### Part 2

<details>

Use `@lru_cache` on the recursive function in part 1.

</details>

## Day 13

Didn't realise the old line of symmetry could still exist pain.

### Part 1

<details>

For each grid, iterate through all possible vertical and horizontal lines to check for a reflection.

To find a horizontal reflection in a 2d array, we can iterate from `range(1, len(grid))`. We can then check if the **end** of `grid[:i]` is equal to the **start** of `grid[i:]`. This can be done with `zip()` in python.

To find vertical reflections, rotate the list 90 degrees with `list(zip(*grid[::-1]))`, and find horizontal reflections as above.

</details>

### Part 2

<details>

For each grid, iterate over all elements, and check for reflections after changing only that element using part 1, while ignoring the original reflection.

</details>


## Day 14

### Part 1

<details>

Iterate through each character in the grid from top to bottom. For every `O`, find the next cell above that is not `.` by iterating, and move the `O` to the last `.` before the non `.` character.

</details>

### Part 2

<details>

First, notice 1 billion is a multiple of 4, so you end on the move before a north roll.

The idea is to find a cycle of stone positions after every 4 rolls (i.e. after every NWSE set of rolls).

To do a single set of NWSE rolls, we can repeat the following 4 times: do part 1, then rotate the grid 90 degrees clockwise.

After finding a cycle, we can predict the exact state within the cycle we end up in after our 1 billion cycles by maths.

</details>

## Day 15

### Part 1

<details>

Implement the specified hash function and run on the list of steps. (IDK what to write here lol)

</details>

### Part 2

<details>

Here, I used a dictionary of dictionaries to store the boxes. The outer dictionary is the box, and the inner dictionary is for the sequence of lenses. (Python `dict`s are ordered since python 3.6)

To remove a lens, simply use `del` keyword on the box and label.

To add/change a lens, just set the box and label to the focal length.

When I say use the box and label, do `boxes_dict[HASH(label)][label]`.

For the focusing power, to get the slot in a box, you can iterate over the inner dictionary in order (i.e. `enumerate(boxes_dict[x].values(), start=1)`)

</details>

## Day 16

### Part 1

<details>

BFS over the grid. Remember to check you haven't visited the current position AND direction before processing the current node.

I used a queue of (position, direction) tuples. Repeatedly pop from queue until empty. For each state, calculate the new position by adding the direction to the position, and calculate the new direction as specified in the problem statement (See match statement). Note this may generate more than one new state. For each new state, check if it has been visited before, if not append to queue.

</details>

### Part 2

<details>

Bruteforce over all starting states.

</details>

## Day 17

### Part 1

<details>

The idea is to do Dijkstra's where nodes are both current position and previous direction.

At each step, you can travel perpendicular to the previous direction, and you can step: 1, 2, or 3 steps. (Note this is in both perpendicular directions).

In python, to implement a priority queue, you can use the builtin `heapq` and use the min-heap, discarding nodes you've already processed.

</details>

### Part 2

<details>

Instead of only being able to step 1, 2, or 3 steps, you can step [4, 10] steps instead.

</details>

## Day 18

Didn't know about shoelace :(. I've added my implementation of a shoelace solution in my code somewhere.

### Part 1

<details>

Ended up maintaining list of intervals at each row in a grid. The idea is that the interval doesn't change until you hit a corner, so you only need to iterate over each row containing a corner.

At each row, sort the corners and pair adjacent ones. (e.g. [4, 6, 1, 8] -> [(1, 4), (6, 8)])
We will call the previous intervals existing intervals, and the intervals generated from the corners new intervals.

There are 5 cases:

  1) The new interval exactly matches an existing interval, in which case the interval is deleted.
  2) The new interval has one edge matching an existing interval, in which case shrink the existing interval to the new interval
  3) The new interval is entirely contained within an existing interval, in which case split the existing interval into 2, with a gap of the new interval
  4) The new interval touches two different existing intervals on either side, in which case merge the two existing intervals
  5) None of the above, in which case add the new interval to the existing intervals.

Getting the area of lines containing no corners is trivial maths. For lines containing corners, you want to find the points that are within either the previous intervals or the current intervals, which are the existing intervals before and after processing the current corners. You can do this by merging the two sets of intervals, which can be done by sorting them and merging overlapping ones.

</details>

### Part 2

<details>

Same as part 1.

</details>

## Day 19

too lazy to use (read learn) z3.

### Part 1

<details>

The works can be represented as a graph, with edges having conditions.

Traverse the graph until you reach a "R" or "A".

To check the condition, you can replace the letter with the part's value, and call `eval` on it.

</details>

### Part 2

<details>

The idea is to generate all paths in the graph, to generate a list of conditions which gets a part accepted.

DFS through the graph, while maintaining a list of current conditions. At each node, for each condition, add the condition to the list of current conditions before traversing to the next node. If you do not travel on that condition, you need to add the inverse to the list of current conditions.

E.g.: for the example: `ex{x>10:one,m<20:two,a>30:R,A}`

Assuming your dfs call looks like: `dfs(node, list_conditions)`, you should have the following calls:

`dfs(one, list_conditions + x>10)`

`dfs(two, list_conditions + x<=10, m<20)`

`dfs(R, list_conditions + x<=10, m>=20, a>30)`

`dfs(A, list_conditions + x<=10, m>=20, a<=30)`

Note at each step, the previous condition was inverted and added.

When you reach `R` or `A`, you can terminate. If you terminate at `A`, add the list of conditions to an overall list.

Now you should have a list of all ranges that reach an `A`. Observe that there are no overlaps between these ranges, since given any part, it must reach only 1 destination, so the path must be unique.

For each set of ranges, you can work out how many values it covers, and add it to a total. You can do this by starting from the base range of `[1, 4000]` for all values, and narrow it down based on each condition.

</details>


## Day 20

Forgot graph was directed when inspecting my input with networkx. Was very confused -_-.

### Part 1

<details>

Store the input as a graph. Also store the inverse of the graph (inputs for each node).

I will use False as low and True as high.

Keep track of what value each node last sent (I will refer to this as the memory). This is initialised to all False.

The idea is to BFS through the graph, keeping track of the value being sent to the current node.

Initialise the queue to broadcaster outputs receiving False.

Dequeue the current node and its input. If the current node is a flip-flop, flip the memory and send the memory value to all children if needed. If the current node is a conjunction, check the memory of all inputs and send the corresponding pulse. Pulses are sent by enqueueing the next node and the value of the pulse i.e. True/False.

You can count pulses sent when dequeueing.

</details>

### Part 2

<details>

Note: Unsure if all inputs are the same, try to read your own input first.

The broadcaster sends inputs to multiple counters, which are collected at the end by `rx` when they all reach maximum value.

First check the stage at which the counters get collected to see how often they pulse. You should end up with a list of primes for each counter. Then you can use Chinese Remainder Theorem to determine when they all pulse at the same time. In my case, since they all pulse at exactly a multiple of the prime, I can just find the lcm.

</details>