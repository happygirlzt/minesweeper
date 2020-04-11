import random
import time
import copy

from config import *

def remove_redundant_clicks(solutions, all_uncovered_neighbors):    
    original_solutions=copy.deepcopy(solutions)
    
    pop_size=len(solutions)
    
    for k in range(pop_size):
        solution=solutions[k]
        
        size=len(solution)
        for i in range(size):
            click_key=str(original_solutions[k][i][0])+'+'+str(original_solutions[k][i][1])
            
            if click_key not in all_uncovered_neighbors:
                continue
            
            for j in range(i + 1, size):
                
                neigh_value=str(original_solutions[k][j][0])+'+'+str(original_solutions[k][j][1])
                                    
                if neigh_value in all_uncovered_neighbors[click_key]:
                    if original_solutions[k][j] in solutions:
                        solutions.remove(original_solutions[k][j])
                
    
# Based on the clicks
# count of clicks smaller, fit more
# count of clicks larger, fit less

def cal_fitness(population):
    '''
    Remove all population whose steps are larger than the threshold
    '''
    min_steps, max_steps = min(map(len, population)), max(map(len, population))
    
    # print('min_steps are {}'.format(min_steps))
    steps_threshold=(min_steps+max_steps)//2
    
    original_pop = copy.deepcopy(population)
    for solution in original_pop:
        if len(solution) > steps_threshold:
            population.remove(solution)
            
    return min_steps


# Based on the cells opened
# more cells opened, fit more
# fewer cells opened, fit less

def fitness_func(ms_board, solutions, pop_fitness):
    original_pop_fitness = copy.deepcopy(pop_fitness)
    
    fitness_threshold = (len(ms_board) * len(ms_board[0]) - BEGINNER_MINES_NUMBER) * 0.75
    for solution in original_pop_fitness:
        score = solution[0]
        if score < fitness_threshold:
            pop_fitness.remove(solution)
            solutions.remove(solution[1])


def generate_parents(ms_board, population, num_parents):
    '''
    Randomly select num_parents parents
    '''
    
    par_list = []
    par_index_set = set()
    
    population_size = len(population)
    
    for parent_num in range(num_parents):
        candidate_index=random.randint(0, population_size - 1)
        candidate=population[candidate_index]
        
        if candidate_index not in par_index_set:
            par_index_set.add(candidate_index)
            par_list.append(candidate)
    
    return par_list


def crossover(parents, offsprings_size):
    '''
    We use single point crossover
    Returns list of offsprings
    '''
    
    parents_size=len(parents)
    offsprings=[]
    for i in range(offsprings_size):
        parent1 = parents[i % parents_size]
        parent2 = parents[(i + 1) % parents_size]
        
        size=min(len(parent1), len(parent2))
        cross_point = random.randint(0, size - 1)
        offsprings.append(parent1[:cross_point] + parent2[cross_point:])

    return offsprings


def mutation(offsprings,rows,cols):
    '''
    randomly change a value
    '''
    for child in offsprings:
        size=len(child)
        index=random.randint(0,size-1)
        
        random_row=random.randint(0,rows-1)
        random_col=random.randint(0,cols-1)
        
        child[index]=[random_row,random_col]