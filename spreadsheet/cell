import datetime

colors = {0: "white",
          1: "black",
          2: "green",
          3: "purple",
          4: "yellow"}

class Cell:
    def __init__(self, value = "", color = 0):
        self.value = value
        self.color:int = color

    def setValue(self, value:str):
        self.value = str(value)

    def setColor(self, color: int):
        if color in range(5):
            self.color = color
        else:
            raise ValueError

    def getValue(self):
        return self.value

    def getColor(self):
        return colors[self.color]

    def toInt(self):
        return int(self.value)

    def toFloat(self):
        return float(self.value)

    def toDate(self):
        return datetime.date(int(self.value[:4]), int(self.value[5:7]), int(self.value[8:]))

    def reset(self):
        self.color = 0
        self.value = ""
