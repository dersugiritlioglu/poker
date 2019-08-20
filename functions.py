# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:58:46 2018

@author: lenovo
"""
import random
import numpy as np
#from player import *

def betting(players, table_money):
    if len(players)<3:
        pass
    else:
        players_to_talk = len(players)
        folded_players = 0
        cur_player = findFirsttoTalk(players)
        #something like a while loop
        decision = int(input('Betting decision:\n0: Check, 1: Raise, 2: Fold'))
        while decision!=0 and decision!=1 and decision!=2:
            print('Enter a correct decision.')
            decision = int(input('Betting decision:\n0: Check, 1: Raise, 2: Fold'))
        if decision==0:
            players_to_talk -= 1
        elif decision==1:
            raiseamount = int(input('How much would you like to raise?'))
            cur_player.decreaseMoney(raiseamount)
            table_money += raiseamount
            players_to_talk = len(players) - 1 - folded_players
        elif decision==2:
            players_to_talk -= 1
            folded_players += 1
            cur_player.set_silent()
            
        #TODO: while players to talk tarzı bişeyle devam edicez, sonra init betting yapılacak
        
            
        pass
    return table_money

def initial_betting(players, sb, bb):
    # copy betting function, but deduct the initial bettings this time
    return table_money

def left_player(players, pos):    
    # pos is the position of the main player
    # this function returns the player on the left of the main player
    leftpos = pos%len(players)
    return players[leftpos]

def findFirsttoTalk(players):
    for i in range(len(players)):
        if players[i].standing == 'bb':
            break
    return left_player(players, i)
    
def numtosuit(num):
	if num == 1:
		return 'Hearts'
	elif num == 2:
		return 'Spades'
	elif num == 3:
		return 'Diamonds'
	elif num == 4:
		return 'Clubs'
	else:
		print("ERROR in numtotype")
		return '-1'

def numtocard(num):
	if num == 1:
		return 'A'
	elif num == 11:
		return 'J'
	elif num == 12:
		return 'Q'
	elif num == 13:
		return 'K'
	else:
		return str(num)
	
def most_occuring(hand):
	# hand = 7x2
	return np.bincount(hand)

def create_type_list(hand):
	types_list = []
	for i in range(14):
		types_list.append(0)
	for i in range(7):
		if types_list[hand[i][1]] == 0 :
			types_list[hand[i][1]] = hand[i][0]
		elif type(types_list[hand[i][1]]) == tuple:
			length = len(types_list[hand[i][1]])
			#initialize tpl
			tpl = (types_list[hand[i][1]][0],)
			for j in range(1,length):
				tpl = (tpl, types_list[hand[i][1]][j])
			types_list[hand[i][0]] = tpl
		else:
			# only 1 item
			types_list[hand[i][1]] = (types_list[hand[i][1]], hand[i][0])
	return types_list
			

			
def isStraightFlush(hand):
	# given hand should be in 7x2 order
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	#most_number = most_number_arr.argmax()
	
	# Special case for ace
	# Only need to consider 10-J-Q-K-A
	if len(most_number_arr) == 14 and most_type_arr[most_type] > 4:
		if most_number_arr[0] and most_number_arr[9] and most_number_arr[10] and most_number_arr[11] and most_number_arr[12]:
			fromaceindices = np.where(hand[:,0]==most_type)[0]
			if 1 in hand[fromaceindices,1] and 9 in hand[fromaceindices,1] and 10 in hand[fromaceindices,1] and 11 in hand[fromaceindices,1] and 12 in hand[fromaceindices,1]:
				
				# bundan sonrası biraz deneme, inner priority için
				if(most_type == 1):
					return True,0
				if(most_type == 2):
					return True,1
				if(most_type == 3):
					return True,2
				if(most_type == 4):
					return True,3
	
	
	if(most_type_arr[most_type] < 5):
		return False, np.inf
	else:
		indices = np.where(hand_t[0] == most_type)
		new = np.zeros(len(indices[0]))
		for i in range(len(new)):
			new[i] = hand_t[1][indices[0][i]]
		new.sort()
		for i in range(len(new)-1):
			if new[i+1]-new[i] != 1:
				return False, np.inf
		maxnum = np.max(new)
		pri = (14- maxnum) * 4 + (most_type-1)
		return True, pri

		
#most_number_arr[most_number] < 5
# hand will be given as a list, 7 as length
#len = len(hand)
#arr = np.zeros([7,2])
#for i in range(len):
#	arr[i][0] = hand[i][0]
#	arr[i][1] = hand[i][1]
#arr_t = arr.transpose()


def isFourOfaKind(hand):
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	most_number = most_number_arr.argmax()
	types_list = create_type_list(hand)
	
	if np.where(most_number_arr>3)[0].shape[0]:
		maxnum = np.max(np.where(most_number_arr>3)[0])
		if maxnum == 1:
			return True, 0
		return True, 14-maxnum
	else:
		return False, np.inf
	
def isFullHouse(hand):
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	most_number = most_number_arr.argmax()
	types_list = create_type_list(hand)
	
	for i in range(14):
		types_list.append(0)
	for i in range(7):
		if types_list[hand[0][1]] == 0 :
			types_list[hand[0][1]] = hand[i][0]
		else:
			types_list[hand[0][1]]
	
	if np.where(most_number_arr>2)[0].shape[0] >= 1 and np.where(most_number_arr>1)[0].shape[0] >= 2:
		
		# dublette bu değişiklikler gerekebilir biraz sorunlu!!!!!
		
		triplet = np.max(np.where(most_number_arr>2)[0][0])
		#triplet_index = np.where(most_number_arr == triplet)[0][0]
		#np.delete(most_number_arr, triplet_index)
		np.delete(most_number_arr, triplet)
		doublet = np.max(np.where(most_number_arr>1)[0])
		if triplet == 1:
			# triplet is ace
			innerpri_aceto2_triplet = 0
		else:
			innerpri_aceto2_triplet = 14-triplet
		
		if doublet == 1:
			# doublet is ace
			innerpri_aceto2_doublet =  1
		else:
			innerpri_aceto2_doublet = 15-triplet
			
		innerpri = 14*(14-innerpri_aceto2_triplet) + (14-innerpri_aceto2_doublet)
		return True, innerpri	
# =============================================================================
# 		triplet_type = type_list[triplet]
# 		doublet_type = type_list[doublet]
# 		if 1 not in triplet_type:
# 			triptype_pri = 3
# 		if 2 not in triplet_type:
# 			triptype_pri = 2
# 		if 3 not in triplet_type:
# 			triptype_pri = 1
# 		if 4 not in triplet_type:
# 			triptype_pri = 0
# 			
# 		if 1 in doublet_type and 2 in doublet_type:
# 			doubtype_pri = 0
			
			
			#Suite bağlı değilmiş - wikipedia
# =============================================================================	
	else:
		return False, np.inf
	
def isFlush(hand):
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	#most_number_arr = most_occuring(hand_t[1])
	#most_number = most_number_arr.argmax()
	types_list = create_type_list(hand)
	
	if(most_type_arr[most_type] < 5):
		return False, np.inf
	else:
		#typepri do not exist
		flushindices = np.where(hand[:,0] == most_type)[0]
		inter = hand[flushindices]
		inter = np.sort(inter, axis=0)
		shp = inter.shape[0]
		realhand = np.zeros(5)
		for i in range(5):
			if inter[shp-1-i][1] == 1:
				inter[shp-1-i][1] = 14
			realhand[i] = 14- (inter[shp-1-i][1] - 1)
			# -2 is just for ranging in [1,13] instead of [2,14] where ace=1, king=2, 2=13
		pri = (14-realhand[0])*14**4 +(14-realhand[1])*14**3 +(14-realhand[2])*14**2 +(14-realhand[3])*14**1 +(14-realhand[4]) 
		return True, pri
	
def isStraight(hand):
	# given hand should be in 7x2 order
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	most_number = most_number_arr.argmax()
	count_straight = 0
	types_list = create_type_list(hand)
	
	# Special case for ace
	# Only need to consider 10-J-Q-K-A
	if len(most_number_arr) == 14:
		if most_number_arr[0] and most_number_arr[10] and most_number_arr[11] and most_number_arr[12] and most_number_arr[13]:
			return True, 0
		
	for i in range(1,len(most_number_arr)):
		flag = most_number_arr[i]-most_number_arr[i-1]
		if flag == 1:
			# a change occured in existence
			if most_number_arr[i]:
				count_straight = 1
			else:
				count_straight = 0
		else:
			# no change
			if most_number_arr[i]:
				count_straight += 1
			else:
				count_straight = 0
		if count_straight == 5:
			pri = 14 - most_number_arr[i]
			return True, pri
		#print("Turn: ", i, "  Count: ", count_straight)
	
	return False, np.inf
	
def isThreeOfaKind(hand):
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	most_number = most_number_arr.argmax()
	types_list = create_type_list(hand)
	
	
	if np.where(most_number_arr>2)[0].shape[0]:
		if most_number == 1:
			most_number = 14
		three_pri = 14-most_number
		# cannot be deuce since not fullhouse
		inter = np.where(most_number_arr<2)[0]
		inter = np.sort(np.where(most_number_arr>0)[0])
		length = len(inter)
		first, second = inter[length-1], inter[length-1]
		
		pri = (14-three_pri)*14**2 + (14-first)*14 + (14-second)
		return True, pri
	else:
		return False, np.inf
	
def isTwoPair(hand):
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	most_number = most_number_arr.argmax()
	types_list = create_type_list(hand)
	
	if np.where(most_number_arr>1)[0].shape[0] >= 2:
		deuces = np.where(most_number_arr>1)[0]
		first, second = deuces[len(deuces) - 1] , deuces[len(deuces) - 2]
		inter = np.sort(np.where(most_number_arr==1)[0])
		side = inter[len(inter)-1]
		if first ==1:
			first = 14
		elif second ==1:
			second = 14
		elif side ==1:
			side = 14
		pri = (14-first)*14**2 + (14-second)*14 + (14-side)
		return True, pri
	else:
		return False, np.inf
	
def isPair(hand):
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	most_number = most_number_arr.argmax()
	types_list = create_type_list(hand)
	
	if np.where(most_number_arr>1)[0].shape[0]:
		pair = np.where(most_number_arr>1)[0]
		maxnum = pair[len(pair)-1]
		single= np.where(most_number_arr>0)[0]
		one, two, three, four = single[len(single) - 2], single[len(single) - 3], single[len(single) - 4] ,single[len(single) - 5]
		pri = (14-maxnum)* 14**4 + (14-one)*14**3 + (14-two)*14**2 + (14-three)*14 + (14-four)
		return True, pri
	else:
		return False, np.inf
	
def isHighCard(hand):
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	most_number = most_number_arr.argmax()
	types_list = create_type_list(hand)
	
	single= np.where(most_number_arr>0)[0]
	maxnum = np.max(single)
	one, two, three, four = single[len(single) - 2], single[len(single) - 3], single[len(single) - 4] ,single[len(single) - 5]
	pri = (14-maxnum)* 14**4 + (14-one)*14**3 + (14-two)*14**2 + (14-three)*14 + (14-four)

	if 1 in hand[:,1]:
		maxnum = 14
		pri = (14-maxnum)* 14**4 + (14-one)*14**3 + (14-two)*14**2 + (14-three)*14 + (14-four)
		return True, pri

	maxnum = np.max(hand[:,1])
	return True, pri
	
def refresh_deck():
	index_list = []
	refresh_index_list(index_list)
	#print (index_list)
	
	
	
	card_list = []
	for i in range(1,5):
		for j in range(1,14):
			card_list.append((i,j))
	
	
	#cards = card_list.copy()
	cards = []
	#shuffle(cards, index_list)
	for i in range(52):
		random_index = random.randint(0,len(index_list)-1) 
		cards.insert(52-len(index_list),card_list[index_list[random_index]-1])
		index_list.remove(index_list[random_index])

	print ("Shuffled!")
	#print (cards)
	refresh_index_list(index_list)
	return(cards)
	
def refresh_index_list(index_list):
	for i in range(1,53):
		index_list.insert(i,i)		

		
# =============================================================================
# def shuffle(cards, index_list):
# 	for i in range(52):
# 		random_index = random.randint(0,len(index_list)-1) 
# 		cards.insert(52-len(index_list),card_list[index_list[random_index]-1])
# 		index_list.remove(index_list[random_index])
# 
# 	print ("Shuffled!")
# 	#print (cards)
# 	refresh_index_list(index_list)
# =============================================================================
	
def distribute_cards(cards, Players):
	# shuffled
	playercount = len(Players)
	new_cards = cards.copy()
	for i in range(playercount):
		Players[i].hand.append(cards[0+i])
		new_cards.remove(cards[0+i])
		Players[i].hand.append(cards[playercount+i])
		new_cards.remove(cards[playercount+i])
	return new_cards
	
def distribute_flop(cards, floor):
	new_cards = cards.copy()
	for i in range(3):
		new_cards.remove(cards[i])
		floor[i][0] = cards[i][0]
		floor[i][1] = cards[i][1]
	return new_cards
	
def distribute_turn(cards, floor):
	new_cards = cards.copy()
	new_cards.remove(cards[0])
	floor[3][0] = cards[0][0]
	floor[3][1] = cards[0][1]
	return new_cards	
	
def distribute_river(cards, floor):
	new_cards = cards.copy()
	new_cards.remove(cards[0])
	floor[4][0] = cards[0][0]
	floor[4][1] = cards[0][1]
	return new_cards
		
def hand_comparison(players, floor):
	#smaller is better
	count_players = len(players)
	better = np.zeros(count_players)
	for i in range(count_players):
		for j in range(i+1, count_players):
			firsthand = players[i].valuehand(floor)
			secondhand = players[j].valuehand(floor)
			if (firsthand[0]<secondhand[0]):
				better[i] +=1
			elif (firsthand[0]>secondhand[0]):
				better[j] +=1
			else: #equal
				if (firsthand[1]<secondhand[1]):
					better[i] +=1
				elif (firsthand[1]>secondhand[1]):
					better[j] +=1
				else:
					better[i] += 0.1 #equal totally
	return better

def printfloor(floor):
	wri = '\n'
	for i in range(len(floor[0:5])):
		suit1 = numtosuit(floor[i][0])
		num1 = numtocard(floor[i][1])
		wri = wri + suit1 + ' ' + num1+ '\n'
	print("\nFloor:\n" ,wri)		 