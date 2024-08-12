import Adafruit_BBIO.ADC as ADC

class InputHandler:
    xPin = "P9_39"
    yPin = "P9_40"
    buttonPin = "P9_38"
    inputs = [None, None, None]


    def __init__(self):
        ADC.setup()

    def getInputs(self):
        self.inputs = [None, None, None]
        bValue = ADC.read(self.buttonPin)
        xValue = ADC.read(self.xPin)
        yValue = ADC.read(self.yPin)

        if bValue < 0.01:
            self.inputs[2] = True
        else:
            self.inputs[2] = False

        if xValue < 0.01:
            self.inputs[0] = "left"
        elif xValue > 0.99:
            self.inputs[0] = "right"
        
        if yValue < 0.01:
            self.inputs[1] = "up"
        elif yValue > 0.99:
            self.inputs[1] = "down"
        
        return self.inputs