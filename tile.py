
class tile:
    isWalkable = None
    isImpassable = None
    isGoal = None
    isPushable = None

    def __init__(self) -> None:
        self.isWalkable = False
        self.isImpassable = False
        self.isGoal = False
        self.isPushable = False
    
    def setWalkable(self, bool):
        self.isWalkable = bool

    def getWalkable(self):
        return self.isWalkable
    
    def setImpassible(self, bool):
        self.isImpassable = bool

    def getImpassible(self):
        return self.isImpassable

    def setGoal(self, bool):
        self.isGoal = bool
    
    def getGoal(self):
        return self.isGoal
    
    def isPushable(self, bool):
        self.isPushable = bool

    def getPushable(self):
        return self.isPushable
    

        