from config import *
from utils import *
import copy


def find_new_click(board):
    res_i = 0
    res_j = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
            else:
                if (board[i][j] != -2) & (board[i][j] != -1):
                    res_i = i
                    res_j = j
    return res_i, res_j


def local_search(clicks, kept_percent, board, mines_number):
    kept_clicks = int(len(clicks) * kept_percent)
    temp_board = copy.deepcopy(board)
    clicks_return = clicks[:kept_clicks]
    number_of_opened_cells = len(board) * len(board[0]) - mines_number
    for i in range(kept_clicks):
        if temp_board[clicks[i][0]][clicks[i][1]] != 0 & temp_board[clicks[i][0]][clicks[i][1]] != -2:
            temp_board[clicks[i][0]][clicks[i][1]] = -2  # opened
            number_of_opened_cells = number_of_opened_cells - 1
        if temp_board[clicks[i][0]][clicks[i][1]] == 0:
            # open multiple cells
            temp_board, number_of_opened_cells = open_cell_zero(clicks[i][0], clicks[i][1], temp_board, number_of_opened_cells)

    while number_of_opened_cells > 0:
        new_i, new_j = find_new_click(temp_board)
        clicks_return.append((new_i, new_j))
        if temp_board[new_i][new_j] != 0 & temp_board[new_i][new_j] != -2:
            temp_board[new_i][new_j] = -2  # opened
            number_of_opened_cells = number_of_opened_cells - 1
        if temp_board[new_i][new_j] == 0:
            # open multiple cells
            temp_board, number_of_opened_cells = open_cell_zero(new_i, new_j, temp_board,
                                                                number_of_opened_cells)
    return clicks_return


def generate_ls_population(population, ms_board, num_mines):
    ls_population = []
    for population_i in population:
        steps = len(population_i)
        best_ls_result = population_i
        for i in LOCAL_SEARCH_KEPT_PERCENT:
            ls_result = local_search(population_i, i, ms_board, num_mines)
            if len(ls_result) < steps:
                steps = len(ls_result)
                best_ls_result = ls_result
        ls_population.append(best_ls_result)
    return ls_population

