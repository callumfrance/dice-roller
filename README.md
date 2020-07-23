Dice-Roller
===========

##### Roll some dice

## What
*Dice-Roller* is designed to make rolling lots of different dice at the same time easy. Roll as many different kinds of dice as you want at the same time, with as many different faces as you want (yes, you can roll a d1 - spoiler alert, it always rolls a 1).

Furthermore, sometimes you just want to add a flat bonus (or several) to a dice roll. *Dice-Roller* lets you do that too.

## How
Lets say you want to roll three 12-sided dice and nine 6-sided dice at the same time, with a flat -17 bonus, and then get their total. Using *Dice-Roller*, simply enter in the following string to generate these dice:
```
3d12  + 9d6 - 17
```
*Dice-Roller* will roll all 12 dice together, producing independent, viewable results for each dice. Finally, these dice are all summed together with the `-17` negative bonus to produce a singular total.

## Statistics
Sometimes you want to know just how likely you are to roll above `X`, below `Y`, or exactly `20`. With *Dice-Roller*, you will be able to view the statistics of a roll before you roll, so you can compare between dice sets and see your probabilities before they become realized. Pretty neat right?
