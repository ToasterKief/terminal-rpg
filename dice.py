#!/usr/bin/python3
"""
This class will be the backbone of our framework's computation. It's a rustic and somewhat ineffecient approach to limit the scope of the system to pseudo-polyhedral randomness but will be tidy and make each roll an instance
"""



import random

class Dice:
    def __init__(self, sides):
        self.sides = sides
    
    def roll(self):
        result = random.randint(1, sides)
        return result
        
    def total(self, times):
        total = 0
        for rolls in range(0, times):
            result = self.roll()
            total += result
        return total
        
