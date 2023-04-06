import random
import time
import os

def mat(s,x,y):
  matrix = []
  for i in range(y):
    matrix.append([s] * x)  # create a 20x20 matrix filled with "X"
  return matrix

snake_head = [random.randint(0, 19),
              random.randint(0, 19)]  # randomly place the snake head
snake_body = [[snake_head[0] - 1, snake_head[1]],
              [snake_head[0] - 2,
               snake_head[1]]]  # place the body of the snake behind the head

direction = "right"


def d(m):
  time.sleep(0.1)
  # clear console with print
  print("\033[H\033[J", end="")
  for i in m:
    print(" ".join(i))

matrix = mat("X",6,6)
def c(i, j,matrix,x,y):
  
  d(matrix)
  if i == y-1 and j == x:
    matrix[i][j - 1] = "0"
    print(d(matrix))
    for i in range(3):
      d(mat("O",x,y))
      time.sleep(0.1)
      d(mat("X",x,y))
      time.sleep(0.1)
    a = mat(" ",x,y)
    a[round((i/2)+1)][round((j/2)-2)] = "E"
    a[round((i/2)+1)][round((j/2)-1)] = "N"
    a[round((i/2)+1)][round((j/2))] = "D"
    d(a)
      
  else:
    if j == x:
      matrix[i][j - 1] = "0"
      matrix[i + 1][0] = ">"
      return c(i + 1, 0,matrix,x,y)
    else:
      if j == 0:
        matrix[i][j] = ">"
        return c(i, j + 1,matrix,x,y)
      else:
        if matrix[i][j] == "X":
          matrix[i][j] = ">"
          matrix[i][j - 1] = "0"
          return c(i, j + 1,matrix,x,y)
        else:
          return d(matrix)


c(0, 0,matrix,6,6)




"""
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.2)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if [i,j] == snake_head: # check if current position is the snake's head
                matrix[i][j] = ">" # if yes, replace with the head symbol
            elif [i,j] in snake_body: # check if current position is the snake's body
                matrix[i][j] = "o" # if yes, replace with the body symbol
            elif matrix[i][j] == "X":
                matrix[i][j] = "-" # if the current position is "X", replace it with "-"
    for row in matrix:
        print(" ".join(row))
    print("\n")
    if direction == "right":
        snake_head[1] += 1 # move the snake to the right
    elif direction == "left":
        snake_head[1] -= 1 # move the snake to the left
    elif direction == "up":
        snake_head[0] -= 1 # move the snake upwards
    elif direction == "down":
        snake_head[0] += 1 # move the snake downwards
    if snake_head[1] == len(matrix[0]) or snake_head[1] == -1: # check if the snake hit the right or left border
        direction = "up" if direction == "right" else "down" # change direction if it did
    elif snake_head[0] == len(matrix) or snake_head[0] == -1: # check if the snake hit the top or bottom border
        direction = "left" if direction == "up" else "right" # change direction if it did
    snake_body.insert(0, list(snake_head)) # add the new head position to the body
    snake_body.pop() # remove the last element of the snake body
    if matrix[snake_head[0]][snake_head[1]] == "-":
        snake_body.append(snake_head) # if the snake hit a "-" then append the current snake_head position to the snake_body
    if not any("X" in row for row in matrix):
        print("The snake ate all the 'X'.")
        break
"""
