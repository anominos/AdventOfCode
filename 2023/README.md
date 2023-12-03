# Advent of code 2023

Another year of massacring my sleep schedule

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