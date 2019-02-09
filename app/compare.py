
from app.models import Car

#a class which can be instantiated to represent all of the data needed
#to be displayed on compare.html

class Diff:
    fType = ""
    ## TODO: add all of the fields for compared values

class ComparePackage:
    owned = Car() #the car the user owns
    theoretical = Car() #the car the user chose to compare
    diff = Diff() #the difference in specs to be calculated

    def __init__(self, owned, theoretical): #constructor
        self.owned = owned
        self.theoretical = theoretical

    def computeDiff(): #computes the difference between owned and theoretical
        ## TODO: compute the differences between owned and theoretical and put them in a Diff object
        return


def compare(car1, car2):
    return ComparePackage(car1, car2)
