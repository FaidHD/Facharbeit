import getData


class GrowCalculation:

    def __init__(self, id, seed):
        self.seed = seed
        self.id = id
        self.fieldData = getData.GetData().Field(self.id)
        self.seedData = getData.GetData().seeds(self.seed)
        self.yCount = []
        self.xCount = []
        self.seedCount = []

    def calcCount(self):
        self.yCount = int(self.fieldData[1]) / int(self.seedData[2])
        self.xCount = int(self.fieldData[2]) / int(self.seedData[3])
        self.seedCount = int(self.xCount * self.yCount)
        return self.seedCount, int(self.xCount), int(self.yCount)
