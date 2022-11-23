import getData


class GrowCalculation:

    def __init__(self, fieldid, seed, tractorid):
        self.fuelCost = None
        self.fuelUsed = None
        self.timeDriven = None
        self.milageDriven = None
        self.avDieselPrice = 1.89
        self.seed = seed
        self.FieldId = fieldid
        self.TractorId = tractorid
        self.fieldData = getData.GetData().Field(self.FieldId)
        self.seedData = getData.GetData().seeds(self.seed)
        self.tractorData = getData.GetData().Tractors(self.TractorId)
        self.yCount = []
        self.xCount = []
        self.seedCount = []

    def calcData(self):
        self.yCount = int(self.fieldData[1])*100 / int(self.seedData[2]) -1
        self.xCount = int(self.fieldData[2])*100 / int(self.seedData[3]) -1
        self.seedCount = int(self.xCount * self.yCount)
        self.milageDriven = float(self.fieldData[2]) * float(self.yCount)
        self.timeDriven = round((self.milageDriven/100) / float(self.tractorData[3]))
        self.fuelUsed = float(self.tractorData[2]) * self.timeDriven
        self.fuelCost = self.fuelUsed * self.avDieselPrice
        return self.seedCount, int(self.xCount), int(self.yCount), round(self.milageDriven), self.timeDriven, self.fuelUsed, self.fuelCost
