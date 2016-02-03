#
# Catan starter code
##
# Alex Rosenfeld
# Jake Dharmasiri
# Will Ieong

class Player:
    def __init__(self, name, color):
        self.name = name
        if str.lower(color) in\
           ["black", "white", "orange", "blue", "red"]:
            self.color = color
        else:
            ## THROW ERROR HERE
            
        # order: brick, ore, sheep, wheat, wood
        self.resources = [0, 0, 0, 0, 0]
        
        # dev_cards = [TBD]
        
    def __repr__(self):
        s = "Name: " + self.name + \
            "\nColor: " + self.color +\
            "\nCurrent resources:\n"
        res = "Number of Bricks: " + str(self.resources[0])
        res += "Number of Ore: " + str(self.resources[1])
        res += "Number of Sheep: " + str(self.resources[2])
        res += "Number of Wheat: " + str(self.resources[3])
        res += "Number of Wood: " + str(self.resources[4])
        return s
    def add_brick(self):
        self.resources[0] += 1

    def add_ore(self):
        self.resources[1] += 1

    def add_sheep(self):
        self.resources[2] += 1

    def add_wheat(self):
        self.resources[3] += 1

    def add_wood(self):
        self.resources[4] += 1

    def subtract_brick(self):
        self.resources[0] -= 1

    def subtract_ore(self):
        self.resources[1] -= 1

    def subtract_sheep(self):
        self.resources[2] -= 1

    def subtract_wheat(self):
        self.resources[3] -= 1

    def subtract_wood(self):
        self.resources[4] -= 1










        
