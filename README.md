# Tower Of Hanoi Random Walk

## Dependencies
Python 3, Numpy

## Usage
python tower_of_hanoi.py number_of_stacks number_disks number_of_iterations

## Description
This python script creates a Tower of Hanoi game, simulates a random walk through the valid move set, and calculates the mean and standard deviation of the center of mass that are calculated at the end of each iteration. The number of stacks, **M**, the number of disks, **N**, and the number of iterations, **T**, are given as command-line inputs. The stacks have position 0, 1, 2, ... **M**-1 and the disks have weights 1, 2, 3, ... **N**. 

The game is initialized with the disks on stack 0 in decreasing order such that the largest disk is at the bottom and the smallest disk is at the top. At each iteration, at least one valid move is possible. A valid move is defined as moving a disk off the top of a stack onto a stack immediately to the left or right as long as the moved disk is smaller than all other disks in the destination stack. The random walk randomly chooses one move out of the set of valid moves and executes it.

At the end of each iteration, the center of mass of all the stacks and disks is calculated. The center of mass is defined as the sum of the products of each disk's weight and stack position divided by the sum of the disk weights. After **T** iterations, the mean and standard deviation of the center of mass distribution is printed to standard output with 10-decimal precision.
