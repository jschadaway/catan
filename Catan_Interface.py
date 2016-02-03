#
# Catan starter code
##
# Alex Rosenfeld
# Jake Dharmasiri
# William Ieong

import catan_classes as cc

def run():
    num_Players = int(input("How many players are playing the game? "))
    player_list = [cc.Player() for i in range(num_Players)]
    for i in range(num_Players):
        player_name = input("What is the name of Player " + str(i) + "? ")
        player_color = input("What color is Player " + str(i) + "? ")
        player_list[i].name = player_name
        player_list[i].color = player_color
    return player_list
        
