#
# Catan_Interface
##
# Alex Rosenfeld
# Jake Dharmasiri
# William Ieong

from catan_classes import *

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
            choice_of_player = int(input("Select a player: " + print_p_options()))
            choice_of_resource = int(input("Select a resource: " + print_r_options()))
            adding = str.lower(input("Would you like to add or subtract " +\
                           resources[choice_of_resource] + "?\n"))
            if adding in ["add", "a", "ad", "addd"]:
                player_list[choice_of_player].add_resource(resources[choice_of_resource])
            elif adding in ["subtract", "sub", "s", "subtrcat"]:
                if player_list[choice_of_player].resources[resources[choice_of_resource]] == 0:
                    print(player_list[choice_of_player].name + " has none of this resource!")
                else:
                    player_list[choice_of_player].subtract_resource(resources[choice_of_resource])
            else:
                print("Please type add or subtract")

        elif action == 1:
            #print(player_list)
            #Do we want this to just print the players? Or perhaps take away
            #Color information

            #Do we want this to display all resources or just for one player?
            s = ""
            print(num_Players[1].name)
            for i in range(num_Players):
                s += num_Players[i].name + "\n" + \
                     + num_Players[i].resources + "\n"
            print(s)

        elif action == 2:
            print("Game over, thank you for using the Catan Companion App")
            return
            
        else:
            print("NEED NEW OPTION!")

def print_major_options():
    s = "\n(0) Edit Resources"
    s += "\n(1) View Resources"
    s += "\n(2) End Program\n"
    return s

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
