#
# Catan starter code
##
# Alex Rosenfeld
# Jake Dharmasiri
# William Ieong

class Player:
    def __init__(self, name, color):
        self.name = name
        if str.lower(color) in\
           ["black", "white", "orange", "blue", "red"]:
            self.color = color
        #else:
            ## THROW ERROR HERE
        
            
        # order: brick, ore, sheep, wheat, wood
        self.resources = {'Bricks': 0, 'Ore': 0, 'Sheep': 0, 'Wheat': 0, 'Wood': 0}
        
        
        # dev_cards = [TBD]
        
    def __repr__(self):
        s = "Name: " + self.name + \
            "\nColor: " + self.color +\
            "\nCurrent resources:\n"
        res = "Number of Bricks: " + str(self.resources['Bricks']) + "\n"
        res += "Number of Ore: " + str(self.resources['Ore']) + "\n"
        res += "Number of Sheep: " + str(self.resources['Sheep']) + "\n"
        res += "Number of Wheat: " + str(self.resources['Wheat']) + "\n"
        res += "Number of Wood: " + str(self.resources['Wood']) + "\n"
        return s + res

    def add_resource(self, resource):
        self.resources[resource] += 1
        
##    
##    def add_brick(self):
##        self.resources[0] += 1
##
##    def add_ore(self):
##        self.resources[1] += 1
##
##    def add_sheep(self):
##        self.resources[2] += 1
##
##    def add_wheat(self):
##        self.resources[3] += 1
##
##    def add_wood(self):
##        self.resources[4] += 1
##
##    def subtract_brick(self):
##        self.resources[0] -= 1
##
##    def subtract_ore(self):
##        self.resources[1] -= 1
##
##    def subtract_sheep(self):
##        self.resources[2] -= 1
##
##    def subtract_wheat(self):
##        self.resources[3] -= 1
##
##    def subtract_wood(self):
##        self.resources[4] -= 1










        
