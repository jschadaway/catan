#
# Catan_Interface
##
# Alex Rosenfeld
# Jake Dharmasiri
# William Ieong

from catan_classes import *
from collections import *

num_Players = 0
player_list = []
resources = ["Bricks", "Ore", "Sheep", "Wheat", "Wood"]

def run():
    global num_Players
    global player_list
    global resources
    
    num_Players = int(input("How many players are playing the game? "))
    player_list = [Player() for i in range(num_Players)]
    
    for i in range(num_Players):
        player_name = input("What is the name of Player " + str(i) + "? ")
        player_color = input("What color is Player " + str(i) + "? ")
        player_list[i].name = player_name
        player_list[i].color = player_color
        
    while True:
        action = int(input("What would you like to do? "\
                                 + print_major_options()))
        if action == 0:
            edit_resources()
        elif action == 1:
            view_resources()

        elif action == 2:
            print("Game over, thank you for using the Catan Companion App")
            return
            
        else:
            print("NEED NEW OPTION!")

## Action functions ##

def edit_resources():
    choice_of_player = int(input("Select a player: " + print_p_options()))
    choice_of_resource = int(input("Select a resource: " + print_r_options()))
    change = (input("Enter by how much you would like " +\
                   resources[choice_of_resource] + " to change:\n"))
    
    if change[0] == "-" and change[1:].isnumeric():
        change = int(change)
        if player_list[choice_of_player].resources[resources[choice_of_resource]] + change >= 0:
            player_list[choice_of_player].change_resource(resources[choice_of_resource], change)
        else:
            print("Please enter a valid numer, " + player_list[choice_of_player].name + \
                  " only has " + str(player_list[choice_of_player].resources[resources[choice_of_resource]]) + \
                  " " + resources[choice_of_resource] + "." )
            #print(player_list[choice_of_player], "has fewer than " + abs(change) + choice_of_resource +\
#                  ". Setting " + player_list[choice_of_player] + "'s " + choice_of_resource + " to 0.")
    elif change.isnumeric():
        change = int(change)
        player_list[choice_of_player].change_resource(resources[choice_of_resource], change)
    else:
        print("Please enter a positive or negative number.")

def view_resources():
    #print(player_list)
    #Do we want this to just print the players? Or perhaps take away
    #Color information

    #Do we want this to display all resources or just for one player?
    s = ""
    for i in range(num_Players):
        print_p_resources(player_list[i])
##        print(player_list[i].name)
##        print(str(player_list[i].resources))
##        print()



## Printing functions ##

def print_major_options():
    s = "\n(0) Edit Resources"
    s += "\n(1) View Resources"
    s += "\n(2) End Program\n"
    return s

def print_p_resources(player):
    print(player)

def print_p_options():
    l = ["(" + str(i) + ") " + \
         player_list[i].name for i in range(num_Players)]
    s = "\n"
    for i in range(len(l)):
        s += l[i] + "\n"
    return s

def print_r_options():
    s = "\n(0) Bricks"
    s += "\n(1) Ore"
    s += "\n(2) Sheep"
    s += "\n(3) Wheat"
    s += "\n(4) Wood\n"
    return s
