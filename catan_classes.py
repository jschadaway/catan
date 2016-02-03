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

    def subtract_resource(self, resource):
        self.resources[resource] -= 1
