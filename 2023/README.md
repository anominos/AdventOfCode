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

</details>
