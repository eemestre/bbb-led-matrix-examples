from copy import deepcopy
import Food

class SnakeHead:
    DIRECTIONS = ["up", "down", "right", "left"]
    MAX_BODY_NUMBER = 63
    zeros = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    
    def __init__(self):
        self.alive = True
        self.won = False
        self.justDied = False
        self.justWon = False
        self.ateFood = False
        self.body = [SnakeBody(3, 2)]
        self.x = 3
        self.y = 3
        self.direction = "down"

    def tick(self, xDirection, yDirection, food):
        # Update snake's first body position
        self.body[0].lastX = self.body[0].x
        self.body[0].lastY = self.body[0].y
        self.body[0].x = self.x
        self.body[0].y = self.y

        # Update snake's head direction
        if xDirection != None:
            if self.direction == "right" and xDirection == "left":
                pass
            elif self.direction == "left" and xDirection == "right":
                pass
            else:
                self.direction = xDirection
        elif yDirection != None:
            if self.direction == "down" and yDirection == "up":
                pass
            elif self.direction == "up" and yDirection == "down":
                pass
            else:
                self.direction = yDirection

        # Update snake's head position based on direction
        if self.direction == "down":
            if self.y == 7:
                self.y = 0
            else:
                self.y += 1
        elif self.direction == "up":
            if self.y == 0:
                self.y = 7
            else:
                self.y -= 1
        elif self.direction == "right":
            if self.x == 7:
                self.x = 0
            else:
                self.x += 1
        elif self.direction == "left":
            if self.x == 0:
                self.x = 7
            else:
                self.x -= 1

        # Check if ate food
        if self.x == food.x and self.y == food.y:
            self.ateFood = True
            newBody = SnakeBody(self.body[-1].x, self.body[-1].y)
            food.eaten = True

        # Update the rest of snake's body position
        for i in range(1, len(self.body)):
            self.body[i].lastX = self.body[i].x
            self.body[i].lastY = self.body[i].y
            self.body[i].x = self.body[i-1].lastX
            self.body[i].y = self.body[i-1].lastY

        # Add new body if ate food
        if self.ateFood:
            self.body.append(newBody)
            self.ateFood = False

        # Check if died
        for b in self.body:
            if self.x == b.x and self.y == b.y:
                self.alive = False
                self.justDied = True
                break
        
        # Check if Won
        if len(self.body) == self.MAX_BODY_NUMBER - 1:
            self.won = True
            self.justWon = True
    
    def render(self):
        grid = deepcopy(self.zeros)
        grid[self.y][self.x] = 1

        for b in self.body:
            grid[b.y][b.x] = 1
        
        return grid

class SnakeBody:
    x = 0
    y = 0
    lastX = 0
    lastY = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y