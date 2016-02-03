#
# Catan starter code
##
# Alex Rosenfeld
# Jake Dharmasiri
# Will Ieong

class Player():
    def __init__(self, name, color):
        self.name = name
        self.color = color
        # order: brick, ore, sheep, wheat, wood
        resources = [0, 0, 0, 0, 0]
        # dev_cards = [TBD]
    def __repr__(self):
        s = "Name: " + name + \
            "\nColor: " + color +\
            "\nCurrent resources:\n"
        return s
