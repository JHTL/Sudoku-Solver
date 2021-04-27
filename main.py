"""
1 2 3 | 4 5 6 | 7 8 9 
4 5 6 | 7 8 9 | 1 2 3
7 8 9 | 1 2 3 | 4 5 6
- - - - - - - - - - -
1 2 3 | 4 5 6 | 7 8 9 
4 5 6 | 7 8 9 | 1 2 3
7 8 9 | 1 2 3 | 4 5 6
- - - - - - - - - - -
1 2 3 | 4 5 6 | 7 8 9 
4 5 6 | 7 8 9 | 1 2 3
7 8 9 | 1 2 3 | 4 5 6

"""

EMPTY_PUZZLE = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]

puzzle = [
    [4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 8, 5],
    [0, 0, 7, 0, 4, 8, 0, 5, 0],
    [0, 0, 1, 3, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 7, 0, 0, 0, 0],
    [8, 6, 0, 0, 0, 0, 9, 0, 3],
    [7, 0, 0, 0, 0, 5, 0, 6, 2],
    [0, 0, 3, 7, 0, 0, 0, 0, 0],
]

#HELPER FUNCTIONS

def print_puzzle(puzzle):
  result = ""
  for y in range(0,9):
    if y%3 == 0 and y != 0:
      result += "- - - - - - - - - - -\n"
    for x in range(0,9):
      if x%3 == 0 and x != 0:
        result += "| "
      result += str(puzzle[y][x]) + " "
    result += "\n"
    
  print(result)

def check_x(puzzle,value, ypos):
  for x in range(0,9):
    if puzzle[ypos][x] == value:
      return False
  return True

def check_y(puzzle,value, xpos):
  for y in range(0,9):
    if puzzle[y][xpos] == value:
      return False
  return True

def check_box(puzzle, value, ypos, xpos):
  tly = ypos//3*3
  tlx = xpos//3*3
  for y in range(tly, tly+3):
    for x in range(tlx, tlx+3):
      if value == puzzle[y][x]:
        return False
  return True

def check_valid(puzzle, value, ypos, xpos):
  return check_x(puzzle, value, ypos) and check_y(puzzle, value, xpos) and check_box(puzzle, value, ypos, xpos)

def find_empty(puzzle):
  for y in range(0,9):
    for x in range(0,9):
      if puzzle[y][x] == 0:
        return y, x
  return None


def solver(puzzle):
  spot = find_empty(puzzle)
  if spot == None:
    return True
  else:
    y, x = spot 
    #After finding an empty spot, input the lowest number(1), and check for validity, and check if it is in the final solution. Cycle through to 9.
    #cycle from 1 to 9, checking for validity each time, and final solution if the number is valid
    
    for value in range(1,10):
      if check_valid(puzzle, value, y, x):
        puzzle[y][x] = value
        if solver(puzzle):
          return True
        else:
          puzzle[y][x] = 0
    return False

solver(puzzle)
print_puzzle(puzzle)


