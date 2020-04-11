from config import *
from population_generation import *

from scipy.special import comb

import ga

if __name__ == '__main__':
    ms_board=BEGINNER_BOARD
    num_mines=BEGINNER_MINES_NUMBER
    
    # key: string row+col: set(neighbors)
    # e.g. [3,4] key: 3+4
    all_uncovered_neighbors={}
    population = generate_population(ms_board, BEGINNER_POPULATION,all_uncovered_neighbors)
    
    num_generations=5
    num_parents=4
    
    global_optimal=len(ms_board)*len(ms_board[0])
    
    for generation in range(num_generations):
        print("Generation {} ".format(generation))
        
        if len(population) == 1:
            break
        
        num_parents=min(num_parents, len(population) // 2)
        best_steps=ga.cal_fitness(population)
        
        parents=ga.generate_parents(ms_board, population, num_parents)
        
        parents_size=len(parents)
        offsprings_size=int(comb(parents_size,2))
        offsprings=ga.crossover(parents, offsprings_size)
        
        #ga.mutation(offsprings,len(ms_board), len(ms_board[0]))
        
        # Create new population
        population=parents+offsprings
        
        ga.remove_redundant_clicks(population,all_uncovered_neighbors)
               
        best_steps=min(min(map(len, population)), best_steps)
        global_optimal=min(best_steps,global_optimal)
        print('{}'.format(population))
        print('best result is {}'.format(best_steps))
        
    print('global optimal is {}'.format(global_optimal))