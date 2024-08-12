import Adafruit_BBIO.GPIO as GPIO
import time, copy

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


def animation0():
    global breathingForward, next, aux, loopCount, breathingVelocity

    if aux >= 0 and aux < breathingVelocity:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]] 
    elif aux >= breathingVelocity and aux < 2*breathingVelocity:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    elif aux >= 2*breathingVelocity and aux < 3*breathingVelocity:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    elif aux >= 3*breathingVelocity and aux < 4*breathingVelocity:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    elif aux >= 4*breathingVelocity:
        next = [[1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]]
    
    if aux >= 10 * breathingVelocity:
        breathingForward = False
        aux = 4 * breathingVelocity
    elif aux == 0 and not breathingForward:
        breathingForward = True
        loopCount += 1

    if breathingForward:
        aux += 1
    else:
        aux -= 1


def animation1():
    global next, aux, loopCount, snakeRight, snakeUp, snakeBody, snakeHead, snakeVelocity

    if aux >= snakeVelocity or snakeHead == [7, 0]:
        if snakeRight:
            if snakeHead[1] < 7:
                snakeHead[1] += 1
            else:
                if snakeUp:
                    if snakeHead[0] > 0:
                        snakeHead[0] -= 1
                    else:
                        snakeHead[0] += 1
                        snakeUp = False
                else:
                    if snakeHead[0] < 7:
                        snakeHead[0] += 1
                    else:
                        snakeHead[0] -= 1
                        snakeUp = True
                snakeRight = False
        else:
            if snakeHead[1] > 0:
                snakeHead[1] -= 1
            else:
                if snakeUp:
                    if snakeHead[0] > 0:
                        snakeHead[0] -= 1
                    else:
                        snakeHead[0] += 1
                        snakeUp = False
                else:
                    if snakeHead[0] < 7:
                        snakeHead[0] += 1
                    else:
                        snakeHead[0] -= 1
                        snakeUp = True
                snakeRight =True
        aux = 0
        next = copy.deepcopy(zeros)
        next[snakeHead[0]][snakeHead[1]] = 1
        next[snakeBody[0]][snakeBody[1]] = 1
        snakeBody = copy.deepcopy(snakeHead)
    
    aux += 1
    
    if snakeHead == [7, 0]:
        loopCount += 1


def tick():
    global currentModeIndex, loopCount, aux 

    if currentModeIndex == 0:
        animation0()
        if loopCount == modeLoopCount[0]:
            nextMode()
            aux = 0
            loopCount = 0
    elif currentModeIndex == 1:
        animation1()
        if loopCount == modeLoopCount[1]:
            nextMode()
            aux = 0
            loopCount = 0


def render():
    global grid, next, rows, columns

    for r in range(0, 8):
        for col in range(0,8):
            if grid[r][col] != next[r][col]:
                if next[r][col] == 1:
                    ledOn(rows[r], columns[col])
                else:
                    ledOff(r, col)
    
    grid = copy.deepcopy(next)


def nextMode():
    global modes, currentModeIndex

    if currentModeIndex == len(modes)-1:
        currentModeIndex = 0
    else:
        currentModeIndex += 1


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

# General control variable
tps = 120
aux = 0
loopCount = 0

# Modes control variables
modes = ["Breathing", "Snake"]
modeLoopCount = [8, 2]
currentModeIndex = 0

# Breathing auxiliar variables
breathingForward = True
breathingVelocity = 6

# Snake auxiliar variables
snakeHead = [7, 0]
snakeBody = [7, 0]
snakeRight = True
snakeUp = True
snakeVelocity = 4

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

old = time.time_ns()
# stop = time.time()

# loop
while True:
    now = time.time_ns()

    if now - old >= 1000000000/tps:
        tick()
        old = now
    
    render()

clearGrid()
GPIO.cleanup()
