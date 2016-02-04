#
# Catan_Interface
##
# Alex Rosenfeld
# Jake Dharmasiri
# William Ieong

import catan_classes as cc

num_Players = int(input("How many players are playing the game? "))
player_list = [cc.Player() for i in range(num_Players)]

def run(): 
    for i in range(num_Players):
        player_name = input("What is the name of Player " + str(i) + "? ")
        player_color = input("What color is Player " + str(i) + "? ")
        player_list[i].name = player_name
        player_list[i].color = player_color
    while True:
        choice_of_player = input("Select a player: " + print_p_options())
        choice_of_resource = input("Select a resource: " + print_r_options())
def print_p_options():
    l = [player_list[i].name for i in range(num_Players)]
    s = ""
    for i in range(len(l)):
        s += l[i]
    return s

def print_r_options():
    s = "\n(*)Add a new player"
    s += "\n(0)Bricks"
    s += "\n(1) Ore"
    s += "\n(2) Sheep"
    s += "\n(3) Wheat"
    s += "\n(4) Wood"
    return s
