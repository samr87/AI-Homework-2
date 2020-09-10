# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:08:39 2020

@author: computer realm
"""
from hw2 import Agent

def main():
    
    bot = Agent("bot1", 0, 0)
    
    print(bot.getName())
    
    
    bot.printLocation()
    
    bot.move("right")
    
    bot.printLocation()
    
    
main()