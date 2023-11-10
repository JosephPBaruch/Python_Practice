#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Joseph Baruch
    CS 212 
    

@author: joseph.baruch
"""

class shoes: 
    def __init__( self, owner, health, popularity ):
        """
            Constructor of the shoe class. Initializes attribute values
        """
        self._owner = owner
        self._health = health
        self._popularity = popularity
                
    def use(self):
        """
            This method "uses" the shoe and decreases its health
        """
        if self._health <= 1: 
            print("Shoe is dead. Buy a new one")
        self._health -= 1
        
    def trending(self, pop):
        """
            This method can change the popularity of the shoe
        """
        self._popularity += pop
        
    def __str__(self):
        """
            This dunder method prints all the attributes of the class. 
        """
        return f"Owner: {self._owner}, Health: {self._health}, Popularity: {self._popularity}"

boots = shoes("Joe", 15, 15) # Create instance of the class
boots.use() # decrease health by one
boots.trending(5) # increase popularity by 5
boots.__str__() # call dunder method