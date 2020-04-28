# Introduction
This repo is the implementation of a memetic algorithm, including a genetic algorithm and local seach for a specific Minesweeper.

## Minesweeper
We defind Minesweeper as an optimization question: given a 2D board, our algorithm returns the minimum number of total clicks to uncover all the empty cells.

### Recap of Minesweeper
A typical Minesweeper is given a m * n board and at the beginning, all the cells are covered. The player should pick cells to open and there are usually two cases that could happen. Assume the cell been clicked is called focused\_cell, the following two cases are given:
1. focused\_cell is safe/empty (not a mine). Then focused\_cell would be uncovered and a number ranging from 1 or 8 will show in this cell. This number indicates the total count of the mines in its 8 directed neighbors (left, right, up, down, upper-left, upper-right, lower-left, lower-right). To be strict, if focused_cell is a corner cell, it has 3 neighbors; if focused_cell  is a border cell, it has 5 neighbors and otherwise, it has 8 neighbors. The same uncovering rule will be applied to focused\_cell’s neighbors until they do not have any neighbor that is a mine. 
2. focused\_cell is a mine. The game will end immediately and the player fails.

# Outline of the Basic Genetic Algorithm
1. Start
Generate random population of n chromosomes (suitable solutions for the problem)
2. Fitness
Evaluate the fitness f(x) of each chromosome x in the population
3. New population: Create a new population by repeating following steps until the new population is complete
    - Selection: Select two parent chromosomes from a population according to their fitness (the better fitness, the bigger chance to be selected)
    - Crossover: With a crossover probability cross over the parents to form a new offspring (children). If no crossover was performed, offspring is an exact copy of parents.
    - Mutation: With a mutation probability mutate new offspring at each locus (position in chromosome).
    - Accepting: Place new offspring in a new population
4. Replace Use new generated population for a further run of algorithm
5. Test If the end condition is satisfied, stop, and return the best solution in current population
6. Loop Go to step 2

Reference: [Genetic Algorithms](https://www.obitko.com/tutorials/genetic-algorithms/ga-basic-description.php)
