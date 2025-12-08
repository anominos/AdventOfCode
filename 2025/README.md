# Advent of code 2025

RIP Global leaderboards.

tbh its a lot less stressful now i dont have to worry about beating codegen but it was fun while it lasted

that being said having gone through the ddoses and seeing llms at the top of the lbs i understand why eric has gotten rid of it

ig i'll still be waking up at 5 for fun...

## Day 1

2:11/4:24

pretty standard. used `+100 % 100` for -ve modulo in python cuz i never remember c vs python semantics, pretty sure i dont need the `+100`.

for pt2, just use a for loop incrementing the dial 1 by 1. bruteforce is always the answer.

## Day 2
10:47/18:44

ok didnt realise the ranges were small i got spooked by large numbers oops

Given range `[a, b]`:

First find the smallest front bit that could be repeated. For pt 1 that would be the first half of the string if the string length is even, or `1000...` to be half the smallest final length (`len(100..) ==  (len(a)+1)//2`) if string length is odd.

Then increment this front bit until the repeated number is bigger than `b`.

## Day 3
3:53/12:23

dp. we love `lru_cache(maxsize=None)`

part 1 you can just find the largest digit in the string (that isnt at the end) then find the largest digit that comes after the first digit.

part 2 for each string `s` use `dp(i, n)` = maximum number formed from `s[i:]` taking `n` digits. base cases: `dp(i, 0) = 0`, `dp(len(s)-1, n) = invalid`

as much as i like glazing lru_cache, it might be easier to manually build the 2d array since the invalid cases are probably easier.

## Day 4

5:09/6:32

its nice to have an array of offsets in my template.

part 1 iterate over every element checking for number of adjacent `@`s.

part 2 wrap part 1 in a while loop, setting forkliftable elements to `.` and keep iterating until no changes are made. its probably possible to set `.` during the iteration rather than at the end.

## Day 5

17:19/24:00

overslept oops.

part 1 iterate over the given ids, and for every id check every range to see if its in one of them

part 2 maintain a list of currently processed ranges. to add a new range, we need to check for overlaps. For every already processed range `(c, d)` and new range to be added `(a, b)`, there are 4 cases:

1) `c<=a<=d<=b`, then just add range `(d+1, b)`
2) `a<=c<=b<=d`, then add range `(a, c-1)`
3) `c<=a<=b<=d`, then dont add any range
4) `a<=c<=d<=b`, then remove the range `(c, d)` and add `(a, b)`

## Day 6
2:54/10:02

me when whitespace matters

part 1 just split every string by whitespace, then iterate over the rows at the same time (using zip or indices)

for part 2, the right to left property can be ignored. iterate over the characters one at a time, keeping track of the current operation. you can then update the grand total either when the operation changes or you see 4 spaces

## Day 7

3:15/5:41

me when my code works first time no testing :o

part 1: We only need to store active paths for each row individually, since only the row before affects the current row.

copy the previous row, but replace `i` with `i+1, i-1` if you have a splitter, and remove duplicates.

part 2: dp. you still only need the previous row though. store the amount of paths that reach each index in the row. for the next row, sum the count for every previous index that updates the next index

## Day 8

10:35/22:18

probably easier approaches but i like dsu

pt 1 create a distance matrix, then sort by distance and add edges to an adjacency list. then floodfill.

p2 2 using suitable fill value for the floodfill (have something where `floodfill[a] = a` for some a in every connected component),
we can use the floodfill as a DSU. Add edges to DSU until we have a single connected component, recording every merge that merges two distinct components. then just take the last recorded merge. (you can also count the components as you go along)