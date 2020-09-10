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
            
        def getName(self):
            
            return self.name
            
            
        def move(self,d):
            
            direc = d
            
            if direc == "left" and self.xPos > -10:
                self.xPos = self.xPos - 1
                
            elif direc == "right" and self.xPos < 10: 
                self.xPos = self.xPos + 1
                
            elif direc == "up" and self.yPos < 10:
                self.yPos = self.yPos + 1
                
            elif direc == "down" and self.yPos > 10:
                self.yPos = self.yPos - 1
                
            else:
                print("There is an obstacle in that direction!")
        
        def printLocation(self):
            
            print("The bot's location is: " + str(self.xPos) + " by " + str(self.yPos) + " on the grid.")
            
        def retXposition(self):
            
            return self.xPos
            
        def retYpos(self):
            
            return self.yPos
        
        #def pickUp(environ):
            
            #if environ == dirty, then pickUp
            
            #else move            
#class Environment:
    
    # determines whether a spot is clean or dirty?
            
            
            
            
            
            