#
# Catan_Interface
##
# Alex Rosenfeld
# Jake Dharmasiri
# William Ieong

import catan_classes as cc

num_Players = 0
player_list = []

def run():
    num_Players = int(input("How many players are playing the game? "))
    player_list = [cc.Player() for i in range(num_Players)]
    for i in range(num_Players):
        player_name = input("What is the name of Player " + str(i) + "? ")
        player_color = input("What color is Player " + str(i) + "? ")
        player_list[i].name = player_name
        player_list[i].color = player_color
    while True:
        action = str.lower(input("What would you like to do? "\
                                 + print_major_options()))
        if action = "edit resources":
            
            choice_of_player = input("Select a player: " + print_p_options())
            choice_of_resource = input("Select a resource: " + print_r_options())
            adding = str.lower(input("Would you like to add or subtract " +\
                           choice_of_resource + "?"))
            if adding in ["add", "a", "ad", "addd"]:
                adding = True
            else:
                adding = False

        elif action = "view resouces":
            ## HERE?
        else:
            print("NEED NEW OPTION!")

def print_major_options():
    s = "(\n0) Edit Resources"
    s += "\n(1) View Resources"
    s += "\n(2) Other option here?"
    return s

def print_p_options():
    l = ["Player number " + str(i) + ": " + \
         player_list[i].name for i in range(num_Players)]
    s = ""
    for i in range(len(l)):
        s += l[i] + "\n"
    return s + "\n"

def print_r_options():
    s = "\n(0) Bricks"
    s += "\n(1) Ore"
    s += "\n(2) Sheep"
    s += "\n(3) Wheat"
    s += "\n(4) Wood\n"
    return s
