import copy


def open_cell_zero(cell_position_x, cell_position_y, board, number_of_opened_cells):
    temp_board = copy.deepcopy(board)
    if temp_board[cell_position_x][cell_position_y] != 0:
        temp_board[cell_position_x][cell_position_y] = -2  # opened
        number_of_opened_cells = number_of_opened_cells - 1
        return temp_board, number_of_opened_cells
    if temp_board[cell_position_x][cell_position_y] == 0:
        temp_board[cell_position_x][cell_position_y] = -2  # opened
        number_of_opened_cells = number_of_opened_cells - 1 # opened
        # Left
        if (cell_position_y - 1 >= 0) & (temp_board[cell_position_x][cell_position_y-1] != -2): # not opened yet
            temp_board, number_of_opened_cells = open_cell_zero(cell_position_x, cell_position_y - 1, temp_board,
                                                                number_of_opened_cells)
        # Right
        if cell_position_y + 1 < len(temp_board[0]):
            if temp_board[cell_position_x][cell_position_y+1] != -2: # not opened yet
                temp_board, number_of_opened_cells = open_cell_zero(cell_position_x, cell_position_y + 1, temp_board,
                                                                    number_of_opened_cells)
        # Down
        if cell_position_x + 1 < len(temp_board):
            if temp_board[cell_position_x+1][cell_position_y] != -2:  # not opened yet
                temp_board, number_of_opened_cells = open_cell_zero(cell_position_x + 1, cell_position_y, temp_board,
                                                                    number_of_opened_cells)
        # Up
        if (cell_position_x - 1 >= 0) & (temp_board[cell_position_x-1][cell_position_y] != -2):  # not opened yet
            temp_board, number_of_opened_cells = open_cell_zero(cell_position_x - 1, cell_position_y, temp_board,
                                                                number_of_opened_cells)
        # Up Left
        if (cell_position_y - 1 >= 0) & (cell_position_x - 1 >= 0) & (temp_board[cell_position_x - 1][cell_position_y - 1] != -2):  # not opened yet
            temp_board, number_of_opened_cells = open_cell_zero(cell_position_x - 1, cell_position_y - 1, temp_board,
                                                                number_of_opened_cells)

        # Up Right
        if (cell_position_y + 1 < len(temp_board[0])) & (cell_position_x - 1 >= 0):
            if temp_board[cell_position_x - 1][cell_position_y + 1] != -2:  # not opened yet
                temp_board, number_of_opened_cells = open_cell_zero(cell_position_x - 1, cell_position_y + 1,
                                                                    temp_board,
                                                                    number_of_opened_cells)
        # Down Left
        if (cell_position_y - 1 >= 0) & (cell_position_x + 1 < len(temp_board)):
            if temp_board[cell_position_x + 1][cell_position_y - 1] != -2:  # not opened yet
                temp_board, number_of_opened_cells = open_cell_zero(cell_position_x + 1, cell_position_y - 1,
                                                                    temp_board,
                                                                    number_of_opened_cells)

        # Down Right
        if (cell_position_y + 1 < len(temp_board[0])) & (cell_position_x + 1 < len(temp_board)):
            if temp_board[cell_position_x + 1][cell_position_y + 1] != -2:  # not opened yet
                temp_board, number_of_opened_cells = open_cell_zero(cell_position_x + 1, cell_position_y + 1,
                                                                    temp_board,
                                                                    number_of_opened_cells)
    return temp_board, number_of_opened_cells


def is_solution(clicks, board, mines_number):
    """
    Check if 'clicks' is a solution
    :param clicks: [(7, 7), (0, 0), (0,7), (7, 0), (4,6), (7, 5)]
    :param board: BEGINNER_BOARD
    :param mines_number: BEGINNER_MINES_NUMBER
    :return: True if this is a solution, otherwise False
    """
    temp_board = copy.deepcopy(board)
    number_of_opened_cells = len(board) * len(board[0]) - mines_number
    for click in clicks:
        if number_of_opened_cells == 0:
            return True
        if temp_board[click[0]][click[1]] == -1: # mine
            return False
        if temp_board[click[0]][click[1]] != 0 & temp_board[click[0]][click[1]] != -2 :
            temp_board[click[0]][click[1]] = -2 # opened
            number_of_opened_cells = number_of_opened_cells - 1
        if temp_board[click[0]][click[1]] == 0:
            # open multiple cells
            temp_board, number_of_opened_cells = open_cell_zero(click[0], click[1], temp_board, number_of_opened_cells)
    if number_of_opened_cells == 0:
        return True
    return False