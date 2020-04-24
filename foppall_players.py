#python3

import random
from namebase import playername

all_players = []

class Player:
	def __init__(self, name,sex, age, position, club, attack, defence, condition, moral, luck, value):
		self.name = name
		self.sex = sex
		self.age = age
		self.position = position
		self.club = club
		self.attack = attack
		self.defence = defence
		self.condition = condition
		self.moral = moral
		self.luck = luck
		self.value = value
		self.injured = 0
		pass
	def printout(self):
		print(self.name, ' ' ,self.age ,' ' ,self.position, ' ', self.club, ' ',self.attack,' ', self.defence )

def new_player():
	newplayer = Player(playername('m'),'m',random.randrange(18,35), 'GK','free agent' ,random.randrange(20), random.randrange(20), random.randrange(20), random.randrange(20), random.randrange(20), random.randrange(1000000))
	all_players.append(newplayer)
	return(newplayer)
	
# for x in range(400):
# 	new_player()

print('-name - age - pos - club - att - def -')

for ea in all_players:
	ea.printout()