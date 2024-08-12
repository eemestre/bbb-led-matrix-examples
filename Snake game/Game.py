import Adafruit_BBIO.GPIO as GPIO
import time
from copy import deepcopy
from Snake import SnakeHead
from Food import Food
from InputHandler import InputHandler

def ledOn(r, col):
    GPIO.output(r, GPIO.LOW)
    GPIO.output(col, GPIO.HIGH)


def ledOff(r, col):
    global next, rows, columns

    rFree = True
    cFree = True

    for i in range(0, 8):
        if next[r][i] == 1:
            rFree = False
        if next[i][col] == 1:
            cFree = False

    if rFree:
        GPIO.output(rows[r], GPIO.HIGH)
    if cFree:
        GPIO.output(columns[col], GPIO.LOW)


def clearGrid():
    global rows, columns

    for i in range(0, 8):
        GPIO.output(rows[i], GPIO.HIGH)
        GPIO.output(columns[i], GPIO.LOW)


def deathScreen():
    global next, aux, loop, snake, food

    if snake.justDied:
        food = None
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 1, 0, 1, 0],
                [0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0]]
        snake.justDied = False
    
    if loop <= 6:
        if aux >= 2:
            loop += 1
            aux = 0
        else:
            aux += 1
    else:
        loop = 0
        snake = SnakeHead()


def winScreen():
    global next, aux, loop, snake, food

    if snake.justWon:
        next = [[0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 1, 1, 0, 0, 1],
                [1, 1, 1, 0, 0, 1, 1, 1]]
        food = None
        snake.justWon = False
    
    if loop <= 6:
        if aux >= 2:
            loop += 1
            aux = 0
        else:
            aux += 1
    else:
        loop = 0
        snake = SnakeHead()


def tick():
    global snake, food, inputs, next, loop

    if snake.alive:
        if snake.won:
            winScreen()
        else:
            snake.tick(inputs[0], inputs[1], food)
            if food.eaten:
                food = Food(snake)
    else:
        deathScreen()


def render():
    global grid, next, rows, columns, period, snake, food

    if not snake.alive:
        pass
    elif snake.won:
        pass
    else:
        snakeGrid = snake.render()
        foodGrid = food.render()
        for i in range(0, 8):
            for j in range(0, 8):
                next[i][j] = snakeGrid[i][j] + foodGrid[i][j]

    for r in range(0, 8):
        for col in range(0,8):
            if grid[r][col] != next[r][col]:
                if next[r][col] == 1:
                    ledOn(rows[r], columns[col])
                else:
                    ledOff(r, col)
        time.sleep(period)
        clearGrid()    


grid = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

next = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

zeros =[[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

# Pinout
rows = ["P8_15", "P8_10", "P8_26", "P8_12", "P9_12", "P8_18", "P9_15", "P8_16"]
columns = ["P8_9", "P9_23", "P9_41", "P8_14", "P8_17", "P8_11", "P8_7", "P8_8"]

# Pin config
for i in range(0, 8):
    GPIO.setup(rows[i], GPIO.OUT)
    GPIO.setup(columns[i], GPIO.OUT)
    GPIO.output(rows[i], GPIO.LOW)
    GPIO.output(columns[i], GPIO.HIGH)
clearGrid()

# General control variables
tps = 4
period = 0.0001
aux = 0
i = InputHandler()
running = True
loop = 0

# Snake and food creation
snake = SnakeHead()
food = Food(snake)

# loop
old = time.time_ns()
while running:
    now = time.time_ns()
    inputs = i.getInputs()

    if now - old >= 1000000000/tps:
        tick()
        old = now

    render()

clearGrid()
GPIO.cleanup()
