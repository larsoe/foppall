#python

import random
from foppall_players import Player, new_player, all_players
from foppall_FC import new_club, all_clubs

for x in range(100):
	new_player()

for x in range(7):
	new_club()

for ea in all_players:
	ea.printout()

for ea in all_clubs:
	ea.printout()

print(all_players[6].name, all_players[6].club)

# def assign_players_to_club(ea):										#function to add club to player object
# 	club = (all_clubs[random.randrange(len(all_clubs))].name)
# 	print(ea.name, '--', club)
# 	return(club)

# for ea in all_players:
# 	ea.club = assign_players_to_club(ea)

def assign_club_players():								#assign 10 players to each club
	print('ASSIGN PLAYERS')
	for ea in all_clubs:
		print(ea.name)											
		for x in range(10):
			ea.players = all_players[random.randrange(len(all_players))]
			ea.players.club = ea.name

			print(ea.name, ea.players.name, ea.players.position, ea.players.club)

assign_club_players()

# print('--- Welcome to Foppall Mngr!---')				#menu system?

# a=1
# for ea in all_clubs:
# 	print(a, 'TEAM', ea.name)
# 	a=a+1
# print('')
# test = input('What team do you want to review? ')

print('')

for ea in all_players:
	if ea.position == 'GK':
		print(ea.name, ea.position, ea.age, ea.club)

print('')
print('PLAYERS IN CLUBS')

for ea in all_players:
	print(ea.name, ' - ', ea.club)

test = all_players[99]

print(test.name, test.age, test.club, test.position)
test.age = test.age+1
print(test.name, test.age, test.club, test.position)

