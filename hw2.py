# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:08:36 2020

@author: computer realm
"""

class Agent:
    
        def __init__(self,n,x,y):
        # this defines the class as self.
        
            self.name = n
            self.xPos = x
            self.yPos = y
            
            
        def move(self,d):
            
            direc = d
            
            if direc == "left": # && left is not a border
                self.xPos = self.xPos - 1
                
            elif direc == "right": # && right is not a border
                self.xPos = self.xPos + 1
                
            elif direc == "up": # && up is not a border
                self.yPos = self.yPos + 1
                
            elif direc == "down": # && down is not a border
                self.yPos = self.yPos - 1
                
            else:
                print("There is an obstacle in that direction!")
        
        def printLocation(self):
            
            print("The bot's location is: " + self.xPos + " by " + self.yPos + " on the grid.")
            
        def retXposition(self):
            
            return self.xPos
            
        def retYpos(self):
            
            return self.yPos
        
        def pickUp():
            
            # if environment firty, then suck
            
            # else environment clean, then move or something, idk.
            
#class Environment:
    
    # determines whether a spot is clean or dirty?
            
            
            
            
            
            