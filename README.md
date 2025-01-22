# Tower of Hanoi Solver

This is a Python implementation of the Tower of Hanoi problem. The script uses recursion to move disks between rods while maintaining the rules of the game.

## How It Works

The Tower of Hanoi is a mathematical puzzle where you have three rods and a number of disks of different sizes. The goal is to move all the disks from the source rod to the target rod following these rules:

1. Only one disk can be moved at a time.
2. A disk can only be moved if it is the uppermost disk on a rod.
3. No disk may be placed on top of a smaller disk.

## Features

- Visualizes the state of the rods after every move.
- Adjustable number of disks by modifying the `NUMBER_OF_DISKS` variable.

## Example

The script is initialized with 5 disks on the source rod (`A`). After running, it prints each step until all disks are moved to the target rod (`C`).

### Initial State:
```text
Source: [5, 4, 3, 2, 1], Auxiliary: [], Target: []
