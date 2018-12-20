# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:58:46 2018

@author: lenovo
"""
import random
import numpy as np
from functions import *
from player import *
print(isStraightFlush)
###################################################################
###################################################################
########################     MAIN     #############################
###################################################################
###################################################################
	

# card values
# 1 = kupa - hearts
# 2 = maça - spade
# 3 = karo - diamond
# 4 = sinek - club
J = 11
Q = 12
K = 13
A = (1,14)


global index_list
global card_list
#def main():

cards = refresh_deck()

players = []

#playercount = int(input("How many players? \n\n"))
playercount = 2 # delete afterwards
for i in range(playercount):
	#name = input("Enter name: ")
	name = str(i+1) + '. oyuncu'
	player = Player(name, i)
	players.append(player)

floor = np.zeros((7,2), dtype=int)

new_cards = distribute_cards(cards, players)

new_cards = distribute_flop(new_cards, floor)
new_cards = distribute_turn(new_cards, floor)
new_cards = distribute_river(new_cards, floor)

better = hand_comparison(players, floor)
print("Better array: \n", better)
printfloor(floor)
for i in range(len(players)):
	print("\nPlayer ", i+1, ": \n", players[i])
	print("Value hand: \n" ,players[i].valuehand(floor))
	print("*******************************************")
	
winner = np.where(better == np.max(better))[0][0]
print("Winner: \n\n", players[winner], "\n\n", players[winner].valuehand(floor)[2])
printfloor(floor)

global index_list
global card_list
#main()"""


