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
