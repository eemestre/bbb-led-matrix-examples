from random import randrange
from copy import deepcopy
import Snake

class Food:
    zeros = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]

    def __init__(self, snake):
        self.eaten = False
        placed = False
        l = [[snake.x, snake.y]]

        for b in snake.body:
            l.append([b.x, b.y])

        while not placed:
            x = randrange(8)
            y = randrange(8)    
            placed = True

            for i in l:
                if [x, y] == i:
                    placed = False
        
        self.x = x
        self.y = y
    
    def render(self):
        grid = deepcopy(self.zeros)
        grid[self.y][self.x] = 1
        return grid