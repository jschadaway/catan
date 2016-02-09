#
# Catan starter code
##
# Alex Rosenfeld
# Jake Dharmasiri
# William Ieong

debug = True
from collections import *

class Player:
    def __init__(self, name="" , color=""):
        self.resources_list = ["Bricks", "Ore", "Sheep", "Wheat", "Wood"]
        self.name = name
        self.color = color

##        if str.lower(color) in\
##           ["black", "white", "orange", "blue", "red"]\:
##            self.color = color
##        else:
##            ## THROW ERROR HERE
##            print("Please select a color that has not been chosen yet")
##            return
        
        # order: brick, ore, sheep, wheat, wood
        self.resources = {'Bricks': 0, 'Ore': 0, 'Sheep': 0, 'Wheat': 0, 'Wood': 0}
        
        # dev_cards = [TBD]

    def __repr__(self):
        s = "Name: " + self.name + \
            "\nColor: " + self.color +\
            "\nCurrent resources:\n"
        for key in self.resources_list:
            s += "Number of " + key + ": " + str(self.resources[key]) + "\n"
        return s

    def change_resource(self, resource, num):
        self.resources[resource] += num

##    def subtract_resource(self, resource, num):
##        self.resources[resource] -= 1


