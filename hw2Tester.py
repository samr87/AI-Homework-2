# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:08:39 2020

@author: computer realm
"""
from hw2 import Agent

def main():
    
    bot = Agent("bot1", 9, 0)
    
    print(bot.getName())
    
    bot.printLocation()
    
    bot.move("right")
    
    bot.printLocation()
    
    bot.move("right")
    
    environ()
    
    
    
def environ():
    
    grid = [[0] * 10 for _ in range(10)]
    
    print(grid)
    
main()