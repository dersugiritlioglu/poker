# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:58:46 2018

@author: lenovo
"""
import random
import numpy as np
from functions import *
from player import *




###################################################################
###################################################################
########################     MAIN     #############################
###################################################################
###################################################################
	

# 3-3-10-2-J varken 7-A 9-K'ya kaybetti? Hata







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
sb = 50
bb = 100
dealer_pos = 0
players = []


#playercount = int(input("How many players? \n"))
playercount = 2 # delete afterwards
while playercount < 2:
    print('Please enter a number greater than 1.')
    #playercount = int(input("How many players? \n"))
    playercount = 2 # delete afterwards
    
for i in range(playercount):
	#name = input("Enter name: ")
    name = str(i+1) + '. oyuncu'
    if playercount>2:
        if i == 0:
            standing = 'dealer'
        elif i == 1:
            standing = 'sb'
        elif i == 2:
            standing = 'bb'
        else:
            standing = 'normal'
    else:
        if i == 0:
            standing = 'dealer, sb'
        elif i == 1:
            standing = 'bb'
        
    player = Player(name=name, position=i, standing=standing)
    players.append(player)

floor = np.zeros((7,2), dtype=int)
playing_players = players
# playing players değil de silent ve talking players yapıcam gibi duruyor

new_cards = distribute_cards(cards, players)
total_money_on_table = initial_betting(playing_players, sb, bb, dealer_pos)
new_cards = distribute_flop(new_cards, floor)
total_money_on_table = betting(playing_players, dealer_pos, total_money_on_table)
new_cards = distribute_turn(new_cards, floor)
total_money_on_table = betting(playing_players, dealer_pos, total_money_on_table)
new_cards = distribute_river(new_cards, floor)
total_money_on_table = betting(playing_players, dealer_pos, total_money_on_table)

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




