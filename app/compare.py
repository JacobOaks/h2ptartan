
class ComparePackage:
    owned = {} #the car the user owns
    theoretical = {} #the car the user chose to compare
    diff = {} #the difference in specs to be calculated

    def __init__(self, owned, theoretical): #constructor
        self.owned = owned
        self.theoretical = theoretical

    #checks the owned and theoretical dictionaries to make sure there are no null values in them
    def checkIntegrity(self):
        for x in self.owned:
            if self.owned[x] is None:
                return False
        for x in self.theoretical:
            if self.theoretical[x] is None:
                return False
        return True

        #computes the difference between owned and theoretical and puts them in a Diff object
        #assumes that the theo is subtracted from the owned (negative means theo is higher and vice versa)
        #for non-numerical values, the data is sent like this: [owned] | [theoretical]
    def computeDiff(self):
        self.diff["cYear"] = self.owned["cYear"] - self.theoretical["cYear"]
        self.diff["fCost"] = self.owned["fCost"] - self.theoretical["fCost"]
        self.diff["fType"] = str(self.owned["fType"]) + " | " + str(self.theoretical["fType"])
        self.diff["hMpg"] = self.owned["hMpg"] - self.theoretical["hMpg"]
        self.diff["cMpg"] = self.owned["cMpg"] - self.theoretical["cMpg"]
        self.diff["comboMpg"] = self.owned["comboMpg"] - self.theoretical["comboMpg"]
        self.diff["transType"] = str(self.owned["transType"]) + " | " + str(self.theoretical["transType"])
        self.diff["coTwo"] = self.owned["coTwo"] - self.theoretical["coTwo"]
        self.diff["saveSpend"] = self.owned["saveSpend"] - self.theoretical["saveSpend"]

def compare(car1, car2):
    comparePackage = ComparePackage(car1, car2)
    if(comparePackage.checkIntegrity() == True):
        comparePackage.computeDiff()
        return comparePackage
    else:
        return None
