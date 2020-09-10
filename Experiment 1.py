from random import randint
from Agent import Agent
avg = 0
def main():
    roomba = Agent(randint(0,9),randint(0,9))
    environment = [[randint(0,1) for i in range(0,10)] for j in range(0,10)]
    p = 0
    for i in environment:
        for j in i:
            p += j
    for i in range(0,50):
        x = roomba.GetLocationX()
        y = roomba.GetLocationY()
        if environment[x][y] != 0:
            environment[x][y] = 0
        if y < 9:
            if environment[x][y+1] != 0:
                roomba.MoveUp()
        elif y > 0:
            if environment[x][y-1] != 0:
                roomba.MoveDown()
        elif x < 9:
            if environment[x+1][y] != 0:
                roomba.MoveRight()
        elif x > 0:
            if environment[x-1][y] != 0:
                roomba.MoveLeft()
        else:
            r = randint(0, 3)
            if r == 0:
                if y < 9:
                    roomba.MoveUp()
                else:
                    roomba.MoveDown()
            elif r == 1:
                if y > 0:
                    roomba.MoveDown()
                else:
                    roomba.MoveUp()
            elif r == 2:
                if x < 9:
                    roomba.MoveRight()
                else:
                    roomba.MoveLeft()
            elif r == 3:
                if x > 0:
                    roomba.MoveLeft()
                else:
                    roomba.MoveRight()
    pe = 0
    for i in environment:
        for j in i:
            pe += j
    pe = p - pe
    performance = (pe/p)*100
    print("Perfomance: %.0f%% cleaner" %performance)
    return performance
for i in range(0,100):
    avg += main()
avg = avg/100
print("Average performance: %.0f%%" %avg)
