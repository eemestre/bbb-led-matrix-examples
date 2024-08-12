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
    global next, aux, animation0_velocity

    if aux >= 0 and aux < animation0_velocity:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 0, 0]]
    elif aux <= animation0_velocity and aux < animation0_velocity * 2:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 0, 0, 0]]
    elif aux <= animation0_velocity * 2 and aux < animation0_velocity * 3:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0]]
    elif aux <= animation0_velocity * 3 and aux < animation0_velocity * 4:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 0, 0]]
    elif aux <= animation0_velocity * 4 and aux < animation0_velocity * 5:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 0]]
    elif aux <= animation0_velocity * 5 and aux < animation0_velocity * 6:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]]
    elif aux <= animation0_velocity * 6 and aux < animation0_velocity * 7:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    elif aux <= animation0_velocity * 7 and aux < animation0_velocity * 8:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1]]
    elif aux <= animation0_velocity * 8 and aux < animation0_velocity * 9:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 1]]
    elif aux <= animation0_velocity * 9 and aux < animation0_velocity * 10:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 1],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 1],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 1]]
    elif aux <= animation0_velocity * 10 and aux < animation0_velocity * 11:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 1]]
    elif aux <= animation0_velocity * 11 and aux < animation0_velocity * 12:
        next = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 0]]
    
    aux += 1
    
    if aux >= animation0_velocity * 12:
        aux = 0


def tick():
    animation0()


def render():
    global grid, next, rows, columns, period

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

# General control variable
tps = 120
period = 0.000125
aux = 0

# Animation 0 aux variables
animation0_velocity = 4

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
#stop = time.time()

# loop
while True:
    now = time.time_ns()

    if now - old >= 1000000000/tps:
        tick()
        old = now

    render()

clearGrid()
GPIO.cleanup()
