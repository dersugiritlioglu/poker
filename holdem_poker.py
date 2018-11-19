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
			if isStraightFlush(self):
				priority = 1
			elif isFourOfaKind(self):
				priority = 2
			elif isFullHouse(self):
				priority = 3
			elif isFlush(self):
				priority = 4
			elif isStraight(self):
				priority = 5
			elif isThreeOfaKind(self):
				priority = 6
			elif isTwoPair(self):
				priority = 7
			elif isPair(self):
				priority = 8
			elif isHighCard(self):
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

	hand_t = hand.transpose()
	most_type_arr = most_occuring(hand_t[0])
	most_type = most_type_arr.argmax()
	most_number_arr = most_occuring(hand_t[1])
	most_number = most_number_arr.argmax()
	if(most_type_arr[most_type] < 5):
		return False
	else:
		indices = np.where(hand_t[0] == most_type)
		new = np.zeros(5)
		for i in range(5):
			new[i] = hand_t[1][indices[0][i]]
		new.sort()
		for i in range(4):
			if new[i+1]-new[i] != 1:
				return False
		return True

		
#most_number_arr[most_number] < 5
# hand will be given as a list, 7 as length
#len = len(hand)
#arr = np.zeros([7,2])
#for i in range(len):
#	arr[i][0] = hand[i][0]
#	arr[i][1] = hand[i][1]
#arr_t = arr.transpose()


def isFourOfaKind(hand):
	return True
	
def isFullHouse(hand):
	return True
	
def isFlush(hand):
	return True
	
def isStraight(hand):
	return True
	
def isThreeOfaKind(hand):
	return True
	
def isTwoPair(hand):
	return True
	
def isPair(hand):
	return True
	
def isHighCard(hand):
	return True	
	
	
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














