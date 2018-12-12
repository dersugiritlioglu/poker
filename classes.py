# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:18:56 2018

@author: lenovo
"""

import random
import numpy as np
from functions import *
#from player import *


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
		
	def valuehand(self, floor):
		"""
		Lower the priority, more likely to win
		"""
		#hand = np.zeros((2,2), dtype=int)
		for i in range(5,7):
			for j in range(2):
				#print("i:" , i , " j:", j)
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
			print(" \nstr. flush")
			#print("Floor: \n", floor)
		elif FourOfaKind:
			print(" \nfour of a kind")
			#print("Floor: \n", floor)
			priority = 2
		elif FullHouse:
			print(" \nfull house")
			#print("Floor: \n", floor)
			priority = 3
		elif Flush:
			print(" \nflush")
			################ aynı durumda renk ve sayı büyüklüklerini check etmek
			#print("Floor: \n", floor)
			priority = 4
		elif Straight:
			
			print(" \nstraight")
			#print("Floor: \n", floor)
			priority = 5
		elif ThreeOfaKind:
			print(" \nthree of a kind")
			#print("Floor: \n", floor)
			priority = 6
		elif TwoPair:
			print(" \ntwo pair")
			#print("Floor: \n", floor)
			priority = 7
		elif Pair:
			print(" \npair")
			#print("Floor: \n", floor)
			priority = 8
		elif HighCard:
			print(" \nhighcard ")
			#print("Floor: \n", floor)
			priority = 9
		else:
			print ("ERROR in hand type")
			#print("Floor: \n", floor)
			return -1
		return priority, innerpri