from random import randint
class Agent():
    def __init__ (self,x,y):
        self.name = ""
        self.__locationX = x
        self.__locationY = y 
    def setName(self,n):
        self.name = n
    def getName(self):
        return self.name
    def MoveRandom(self):
        self.__locationY = randint(0,10)
        self.__locationX = randint(0,10)
    def MoveUp(self):
        self.__locationY += 1
    def MoveDown(self):
        self.__locationY -= 1
    def MoveLeft(self):
        self.__locationX -= 1
    def MoveRight(self):
        self.__locationX += 1
    def GetLocationX(self):
        return self.__locationX
    def GetLocationY(self):
        return self.__locationY
