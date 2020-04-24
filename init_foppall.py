#python

from foppall_players import new_player, all_players
from foppall_FC import new_club, all_clubs

for x in range(400):
	new_player()

for x in range(20):
	new_club()


for ea in all_players:
	ea.printout()

for ea in all_clubs:
	ea.printout()