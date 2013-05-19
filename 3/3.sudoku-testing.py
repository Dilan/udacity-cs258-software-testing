import random
import copy
import time
import math

depth = 0

# SPECIFICATION:
#
# check_sudoku() determines whether its argument is a valid Sudoku
# grid. It can handle grids that are completely filled in, and also
# grids that hold some empty cells where the player has not yet
# written numbers.
#
# First, your code must do some sanity checking to make sure that its
# argument:
#
# - is a 9x9 list of lists
#
# - contains, in each of its 81 elements, an integer in the range 0..9
#
# If either of these properties does not hold, check_sudoku must
# return None.
#
# If the sanity checks pass, your code should return True if all of
# the following hold, and False otherwise:
#
# - each number in the range 1..9 occurs only once in each row 
#
# - each number in the range 1..9 occurs only once in each column
#
# - each number the range 1..9 occurs only once in each of the nine
#   3x3 sub-grids, or "boxes", that make up the board
#
# This diagram (which depicts a valid Sudoku grid) illustrates how the
# grid is divided into sub-grids:
#
# 5 3 4 | 6 7 8 | 9 1 2
# 6 7 2 | 1 9 5 | 3 4 8
# 1 9 8 | 3 4 2 | 5 6 7 
# ---------------------
# 8 5 9 | 7 6 1 | 4 2 3
# 4 2 6 | 8 5 3 | 7 9 1
# 7 1 3 | 9 2 4 | 8 5 6
# ---------------------
# 9 6 1 | 5 3 7 | 0 0 0
# 2 8 7 | 4 1 9 | 0 0 0
# 3 4 5 | 2 8 6 | 0 0 0
# 
# Please keep in mind that a valid grid (i.e., one for which your
# function returns True) may contain 0 multiple times in a row,
# column, or sub-grid. Here we are using 0 to represent an element of
# the Sudoku grid that the player has not yet filled in.

# check_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

valid_unsolved =[
         [5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,0,3,4,8],
         [1,9,8,0,4,2,5,6,7],
         [0,0,0,0,0,0,4,2,0],
         [4,2,6,0,5,0,7,9,1],
         [7,1,0,9,2,0,0,0,6],
         [9,0,0,0,3,7,2,0,4],
         [2,0,0,0,0,0,0,3,5],
         [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

# from 
ultra_hard =[
  [8,0,0,0,0,0,0,0,0],
  [0,0,3,6,0,0,0,0,0],
  [0,7,0,0,9,0,2,0,0],
  [0,5,0,0,0,7,0,0,0],
  [0,0,0,0,4,5,7,0,0],
  [0,0,0,1,0,0,0,3,0],
  [0,0,1,0,0,0,0,6,8],
  [0,0,8,5,0,0,0,1,0],
  [0,9,0,0,0,0,4,0,0]]


def check_sudoku(grid):
    ###Your code here.
    # there are 9 rows
    if len(grid) != 9:
      return None

    # each row has 9 elements
    for row in grid:
      if len(row) != 9:
        return None

    # sanity check - make sure each element in grid is digit between 0 and 9
    for row in grid:
      for cell in row:
        if cell not in range(0, 9+1):
          return None

    # test validity of each row
    for row in grid:
      if not group_is_valid(row):
        return False

    # test validity of each column
    for col_number in range(0, 9):
      column = [row[col_number] for row in grid]
      if not group_is_valid(column):
        return False

    # test validity of each sub-grid
    for sub_grid_row_offset in [0, 3, 6]:
      for sub_grid_col_offset in [0, 3, 6]:
        sub_grid = []
        for row_number in [row + sub_grid_row_offset for row in [0, 1, 2]]:
          for col_number in [col + sub_grid_col_offset for col in [0, 1, 2]]:
            sub_grid.append(grid[row_number][col_number])
        if not group_is_valid(sub_grid):
          return False

    return True

def print_grid(grid):
    for row in grid:
      print ' '.join([str(cell) for cell in row])
    print "\n"


def group_is_valid(group):
    # group should have 9 elements - otherwise getting this far indicates error in test code
    if len(group) != 9:
      return False

    # don't care about zeros
    non_zeros = filter(lambda i: i != 0, group)

    # each element should be unique
    if len(non_zeros) != len(set(non_zeros)):
      return False

    # each element should be a digit between 1 and 9 inclusive
    for i in non_zeros:
      if i not in (range(1, 9+1)):
        return False

    return True


def solve_sudoku(grid, blank_cell_coordinates = []):

  global depth

  check_result = check_sudoku(grid)

  if check_result is None:
    print "Invalid grid"
    exit()

  if check_result == False:
    return

  if len(blank_cell_coordinates) == 0:
    # might be the first run, or it might be solved
    blank_cell_coordinates = find_coordinates_of_blank_cells(grid)
    if len(blank_cell_coordinates) == 0:
      print 'Solved'
      print 'depth', depth
      print_grid(grid)
      return True

  # iterate through all the next moves, recursing deeper if the move is valid
  target_cell_coordinates = blank_cell_coordinates.pop()
  for i in find_allowed_numbers(grid, target_cell_coordinates):
    grid[target_cell_coordinates[0]][target_cell_coordinates[1]] = i

    depth = depth + 1
    if solve_sudoku(grid, blank_cell_coordinates):
      return True
    depth = depth - 1

    grid[target_cell_coordinates[0]][target_cell_coordinates[1]] = 0

  blank_cell_coordinates.append(target_cell_coordinates)

  return


def find_coordinates_of_blank_cells(grid):
  blank_cell_coordinates = []
  for row_number, row in enumerate(grid):
    for cell_number, cell in enumerate(row):
      if cell == 0:
        blank_cell_coordinates.append((row_number, cell_number))

  return blank_cell_coordinates


def find_allowed_numbers(grid, coord):
  row_number = coord[0]
  col_number = coord[1]
  allowed_moves = set(range(1, 9+1))
  
  allowed_moves = allowed_moves - set(grid[row_number])
  for i in range(0, 9):
    allowed_moves.discard(grid[i][col_number])

  allowed_moves = allowed_moves - set(find_subgrid_of_coord(grid, coord))
  return allowed_moves


def find_subgrid_of_coord(grid, coord):
  sub_grid_row_offset = find_subgrid_offset_for_coord(coord[0])
  sub_grid_col_offset = find_subgrid_offset_for_coord(coord[1])
  sub_grid = []
  for row_number in [row + sub_grid_row_offset for row in [0, 1, 2]]:
    for col_number in [col + sub_grid_col_offset for col in [0, 1, 2]]:
      sub_grid.append(grid[row_number][col_number])
  return sub_grid


def find_subgrid_offset_for_coord(coord):
  return int(math.floor(coord*1.0/3))*3


def test():
  grid = [
         [5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [0,0,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]
  assert set(find_subgrid_of_coord(grid, (0, 0))) == set([5, 3, 4, 6, 7, 2, 1, 9, 8])
  assert set(find_subgrid_of_coord(grid, (6, 7))) == set([2, 8, 4, 6, 3, 5, 1, 7, 9])
  assert set(find_subgrid_of_coord(grid, (4, 7))) == set([4, 2, 3, 7, 9, 1, 8, 5, 6])

  assert find_subgrid_offset_for_coord(0) == 0
  assert find_subgrid_offset_for_coord(1) == 0
  assert find_subgrid_offset_for_coord(2) == 0
  assert find_subgrid_offset_for_coord(3) == 3
  assert find_subgrid_offset_for_coord(4) == 3
  assert find_subgrid_offset_for_coord(5) == 3
  assert find_subgrid_offset_for_coord(6) == 6
  assert find_subgrid_offset_for_coord(7) == 6
  assert find_subgrid_offset_for_coord(8) == 6

  grid = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]]

  assert find_allowed_numbers(grid, (0, 8)) == set([1, 3, 4, 5, 6, 7, 9])
  assert find_allowed_numbers(grid, (4, 4)) == set([2, 3, 6, 8])


t1 = time.time()
solve_sudoku(easy)
t2 = time.time()
print t2 - t1, 'seconds'


