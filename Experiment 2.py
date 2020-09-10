import random
from Agent import Agent
avg = 0
def main():
    environment = [[random.randint(0,1) for i in range(0,10)] for j in range(0,10)]
    roomba = Agent(random.randint(0,9),random.randint(0,9))
    p = 0
    for i in environment:
        for j in i:
            p += j
    for i in range(0,50):
        dirty = roomba.Perceive(environment)
        if dirty:
            roomba.Clean(environment)
        else:
            roomba.DoNothing()
        roomba.MoveRandom()
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
