from config import *
from population_generation import *
from scipy.special import comb
from local_search import *

import ga

if __name__ == '__main__':
    ms_board = HARD_BOARD
    num_mines = HARD_MINES_NUMBER
    
    # key: string row+col: set(neighbors)
    # e.g. [3,4] key: 3+4
    all_uncovered_neighbors={}
    population = generate_population(ms_board, BEGINNER_POPULATION,all_uncovered_neighbors)
    
    num_generations=5
    num_parents=4
    
    global_optimal=len(ms_board)*len(ms_board[0])
    optimal_ga = []
    optimal_ls = []

    for generation in range(num_generations):
        if len(population) == 1:
            break
        print("Generation {} ".format(generation))

        num_parents=min(num_parents, len(population) // 2)
        best_steps=ga.cal_fitness(population)
        
        parents=ga.generate_parents(ms_board, population, num_parents)
        
        parents_size=len(parents)
        offsprings_size=int(comb(parents_size,2))
        offsprings=ga.crossover(parents, offsprings_size)
        
        #ga.mutation(offsprings,len(ms_board), len(ms_board[0]))
        
        # Create new population
        population=parents+offsprings
        
        ga.remove_redundant_clicks(population, all_uncovered_neighbors)

        # print('population = {}'.format(population))
        print('population shape = {}'.format(shape_of_population(population)))
        optimal_ga.extend(shape_of_population(population))

        local_search_population = generate_ls_population(population, ms_board, num_mines)
        # print('local_search_population={}'.format(local_search_population))
        print('local_search_population shape = {}'.format(shape_of_population(local_search_population)))
        optimal_ls.extend(shape_of_population((local_search_population)))

    # best_steps=min(min(map(len, population)), best_steps)
        # global_optimal=min(best_steps,global_optimal)
        # print('{}'.format(population))
        # print('best result is {}'.format(best_steps))
        
    # print('global optimal is {}'.format(global_optimal))
    print('optimal GA = {}'.format(min(optimal_ga)))
    print('optimal LS = {}'.format(min(optimal_ls)))