"""
Let's play poker!
"""

import random
import numpy as np

class Player:

	decision = 'Fold'
	
	def __init__(self, name, position, money= 10000, playing = True):
		self.name = name
		self.money = money
		self.hand = []
		self.position = position
		
	def Fold(self):
		self.decision = 'Fold'
		self.hand = []
	def Call(self, amount):
		self.decision = 'Call'
		#self.money -= amount
	def Raise(self, amount):
		self.decision = 'Raise'
		#self.money -= amount
	def Bop(self):
		self.decision = 'Bop'
	def All_in(self):
		self.decision = 'All in'
		#self.money = 0
	def __repr__(self):
		suit1 = numtosuit(self.hand[0][0])
		suit2 = numtosuit(self.hand[1][0])
		num1 = numtocard(self.hand[0][1])
		num2 = numtocard(self.hand[1][1])
		hand = suit1 + ' ' + num1+ ', ' + suit2 + ' ' +num2 
		return "Name: " + self.name + "\nMoney: " + str(self.money) + "\nHand: " + hand + "\nPosition: " + str(self.position)
#class Hand:
	"""
	Hand is defined by the 2 cards in one's hand plus the table
	"""
#	def __init__(self):
#		self.hand = []
		
	def typehand_andfloor(self, floor):
		"""
		Lower the priority, more likely to win
		"""
		#hand = np.zeros((2,2), dtype=int)
		for i in range(5,7):
			for j in range(2):
				print("i:" , i , " j:", j)
				floor[i][j] = self.hand[i-5][j]
		

		
		# APPEND THE FLOOR
		
		
		StraightFlush, innerpri 	= isStraightFlush(floor)
		if not StraightFlush:
			FourOfaKind, innerpri 		= isFourOfaKind(floor)
			if not FourOfaKind:
				FullHouse, innerpri 		= isFullHouse(floor)
				if not FullHouse:
					Flush, innerpri 			= isFlush(floor)
					if not Flush:
						Straight, innerpri 			= isStraight(floor)
						if not Straight:
							ThreeOfaKind, innerpri 		= isThreeOfaKind(floor)
							if not ThreeOfaKind:
								TwoPair, innerpri			= isTwoPair(floor)
								if not TwoPair:
									Pair, innerpri				= isPair(floor)
									if not Pair:
										HighCard, innerpri 			= isHighCard(floor)			
		
		if StraightFlush:
			priority = 1
			print(" str. flush")
		elif FourOfaKind:
			print(" four of a kind")
			priority = 2
		elif FullHouse:
			print(" full house")
			priority = 3
		elif Flush:
			print(" flush")
			################ aynı durumda renk ve sayı büyüklüklerini check etmek
			priority = 4
		elif Straight:
			
			print(" straight")
			priority = 5
		elif ThreeOfaKind:
			print(" three of a kind")
			priority = 6
		elif TwoPair:
			print(" two pair")
			priority = 7
		elif Pair:
			print(" pair")
			priority = 8
		elif HighCard:
			print("highcard ")
			priority = 9
		else:
			print ("ERROR in hand type")
			return -1
		return priority, innerpri

#def most_common(lst):
#    return max(set(lst), key=lst.count)

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
		triplet = np.max(np.where(most_number_arr>2)[0])
		triplet_index = np.where(most_number_arr == triplet)[0][0]
		np.delete(most_number_arr, triplet_index)
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
			
		innerpri = 14*innerpri_aceto2_triplet + innerpri_aceto2_doublet
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
		pri = realhand[0]*14**4 +realhand[1]*14**3 +realhand[2]*14**2 +realhand[3]*14**1 +realhand[4] 
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
		
		pri = three_pri*14**2 + first*14 + second
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
		maxnum = pair[len(pair)]
		single= np.where(most_number_arr>1)[0]
		one, two, three, four = single[len(single) - 1], single[len(single) - 2], single[len(single) - 3], single[len(single) - 4]
		pri = maxnum* 14**4 + one*14**3 + two*14**2 + three*14 + four
		return True, pri
	else:
		return False, np.inf
	
def isHighCard(hand):
	types_list = create_type_list(hand)
	
	if 1 in hand[:,1]:
		return True, 0
	maxnum = np.max(hand[:,1])
	return True, 14-maxnum
	
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
		
def hand_comparison(hand1, hand2):
		
	#hand.type		
	return hand1
	return hand2
	



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
	name = str(i) + '. oyuncu'
	player = Player(name, i)
	players.append(player)

floor = np.zeros((7,2), dtype=int)
new_cards = distribute_cards(cards, players)
new_cards = distribute_flop(new_cards, floor)
print(floor)
new_cards = distribute_turn(new_cards, floor)
print(floor)
new_cards = distribute_river(new_cards, floor)
print(floor)
global index_list
global card_list
#main()



