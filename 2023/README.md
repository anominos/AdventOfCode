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