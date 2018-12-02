"""
Let's play poker!
"""

import random
import numpy as np

class Player:

	decision = 'Fold'
	
	def __init__(self, name, money, position):
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
	
	class Hand:
		"""
		Hand is defined by the 2 cards in one's hand plus the table
		"""
		
		def type(self):
			"""
			Lower the priority, more likely to win
			"""
			StraightFlush, innerpri 	= isStraightFlush(self)
			if not StraightFlush:
				FourOfaKind, innerpri 		= isFourOfaKind(self)
				if not FourOfaKind:
					FullHouse, innerpri 		= isFullHouse(self)
					if not FullHouse:
						Flush, innerpri 			= isFlush(self)
						if not Flush:
							Straight, innerpri 			= isStraight(self)
							if not Straight:
								ThreeOfaKind, innerpri 		= isThreeOfaKind(self)
								if not ThreeOfaKind:
									TwoPair, innerpri			= isTwoPair(self)
									if not TwoPair:
										Pair, innerpri				= isPair(self)
										if not Pair:
											HighCard, innerpri 			= isHighCard(self)			
			
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
			return priority

#def most_common(lst):
#    return max(set(lst), key=lst.count)

def most_occuring(hand):
	# hand = 7x2
	return np.bincount(hand)

			
def isStraightFlush(hand):
	# given hand should be in 7x2 order
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	#most_number = most_number_arr.argmax()
	
	# Special case for ace
	# Only need to consider 10-J-Q-K-A
	if len(most_number_arr) == 13 and most_type_arr[most_type] > 4:
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
		pri = (13- maxnum) * 4 + (most_type-1)
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
	
	if np.where(most_number_arr>3)[0].shape[0]:
		maxnum = np.max(np.where(most_number_arr>3)[0])
		if maxnum == 1:
			return True, 0
		return True, 13-maxnum
	else:
		return False, np.inf
	
def isFullHouse(hand):
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	most_number = most_number_arr.argmax()
	
	if np.where(most_number_arr>2)[0].shape[0] >= 1 and np.where(most_number_arr>1)[0].shape[0] >= 2:
		return True
	else:
		return False, np.inf
	
def isFlush(hand):
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	#most_number_arr = most_occuring(hand_t[1])
	#most_number = most_number_arr.argmax()
	if(most_type_arr[most_type] < 5):
		return False, np.inf
	else:
		return True
	
def isStraight(hand):
	# given hand should be in 7x2 order
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	most_number = most_number_arr.argmax()
	count_straight = 0
	print(most_number_arr)
	
	# Special case for ace
	# Only need to consider 10-J-Q-K-A
	if len(most_number_arr) == 13:
		if most_number_arr[0] and most_number_arr[9] and most_number_arr[10] and most_number_arr[11] and most_number_arr[12]:
			return True
		
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
			return True
		print("Turn: ", i, "  Count: ", count_straight)
	
	return False, np.inf
	
def isThreeOfaKind(hand):
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	most_number = most_number_arr.argmax()
	
	if np.where(most_number_arr>2)[0].shape[0]:
		return True
	else:
		return False, np.inf
	
def isTwoPair(hand):
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	most_number = most_number_arr.argmax()
	
	if np.where(most_number_arr>1)[0].shape[0] >= 2:
		return True
	else:
		return False, np.inf
	
def isPair(hand):
	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	most_number = most_number_arr.argmax()
	
	if np.where(most_number_arr>1)[0].shape[0]:
		return True
	else:
		return False, np.inf
	
def isHighCard(hand):
	if 1 in hand[:,1]:
		return True, 0
	maxnum = np.max(hand[:,1])
	return True, 13-maxnum
	
	
def refresh_index_list(index_list):
	for i in range(1,53):
		index_list.insert(i,i)		

		
def shuffle(cards):
	for i in range(52):
		random_index = random.randint(0,len(index_list)-1) 
		cards.insert(52-len(index_list),card_list[index_list[random_index]-1])
		index_list.remove(index_list[random_index])

	print ("Shuffled!")
	#print (cards)
	refresh_index_list(index_list)
	
def hand_comparison(hand1, hand2):
		
	
	return hand1
	return hand2
	
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
index_list = []
refresh_index_list(index_list)
#print (index_list)


global card_list
card_list = []
for i in range(1,5):
	for j in range(1,14):
		card_list.append((i,j))


#cards = card_list.copy()
cards = []
shuffle(cards)


#cards.remove((1,1))
#print ("cards:" , len(cards),"cardlist", len(card_list))














