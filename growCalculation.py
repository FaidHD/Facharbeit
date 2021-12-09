import getData
import getData as gD


class GrowCalculation:

    def __init__(self, id, seed):
        self.seed = seed
        self.id = id
        self.reihenabstand = []
        self.kornabstand = []
        self.fieldHeight = []
        self.fieldWidth = []
        self.yCount = []
        self.xCount = []
        self.seedCount = []

    def calcCount(self):
        print(self.seed)
        print(self.id)
        self.reihenabstand = getData.GetData().seeds(self.seed)[3]
        self.fieldWidth = getData.GetData().Field(self.id)[2]
        self.kornabstand = getData.GetData().seeds(self.seed)[2]
        self.fieldHeight = getData.GetData().Field(self.id)[1]
        self.yCount =  self.fieldHeight / self.kornabstand
        self.xCount = self.fieldWidth / self.reihenabstand
        self.seedCount = self.xCount * self.yCount
        return self.seedCount
