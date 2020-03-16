# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:32:23 2019

@author: gy19sr

Agent framework
"""

import random

class Agent: #the drunks that will move, create density and stop
    def __init__ (self, environment, agents, agentID, environment2):
        
        self.x = random.randint(128,148)
        #the full x range of the pubs location 
        self.y = random.randint(138,159)
        #the full y range of the pubs location 
        #agent starts leaving from random spot in pub
        self.environment = environment #the environment is what is listed in the model, used by the agents
        self.agents = agents #used 
        self.agentID = agentID #used 
        self.environment2 = environment2 #the environment is what is listed in the model, used to make the density map

        
    def __str__(self): #
        return str(self.y) + " " + str(self.x) #set responses to read as a string not object

    
    def move(self):     
     
        if random.random() < 0.5:
            self.y = (self.y + 1) 
        else:
            self.y = (self.y - 1) 
            #move randomly along the y axis
        if self.y < 0:
            self.y = 0
        if self.y > 299:
            self.y = 299
            # set the y boundaries like a fence so agents don't go too far away from home     
            
            
            
        if random.random() < 0.5:
            self.x = (self.x + 1) 
        else:
            self.x = (self.x - 1) 
            #move randomly along the x axis
        if self.x < 0:
            self.x = 0
        if self.x > 299:
            self.x = 299
            # set the x boundaries like a fence so agents don't go too far away from home

            
            
    def density(self):
        if self.environment2[self.y][self.x] >= 0: #no matter the value of the environement as long as it's positive
            self.environment2[self.y][self.x] += 1 #add a density step to the environment

     
            
    def stop(self): #set the x and y equal to its self
        self.x = self.x
        self.y = self.y
        
        #keep the x and y locations the same
    
