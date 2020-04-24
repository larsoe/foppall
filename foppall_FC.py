#python3

import random
all_clubs = []

class FC:
	def __init__(self, name):
		self.name = name
		self.points = 0
		self.league = 0
		self.players = []
	def printout(self):
		print(self.name, ' ', self.points)



cities = [
'London',
'Birmingham',
'Glasgow',
'Liverpool',
'Bristol',
'Manchester',
'Sheffield',
'Leeds',
'Edinburgh',
'Leicester',
'Coventry',
'Bradford',
'Cardiff',
'Belfast',
'Nottingham',
'Kingston upon Hull',
'Newcastle upon Tyne',
'Stoke-on-Trent',
'Southampton',
'Derby',
'Portsmouth',
'Brighton',
'Plymouth',
'Northampton',
'Reading',
'Luton',
'Wolverhampton',
'Bolton',
'Aberdeen',
'Bournemouth',
'Norwich',
'Swindon',
'Swansea',
'Milton Keynes',
'Southend-on-Sea',
'Middlesbrough',
'Peterborough',
'Sunderland',
'Warrington',
'Huddersfield',
]

FC_ending = [

'United',
'F.C.',
'Thursday',
'City',
'Hotspur',
'Wanderers',
'Town',
]


def new_club():
	club_name = cities[random.randrange(len(cities))] + ' ' + FC_ending[random.randrange(0,len(FC_ending))]
	all_clubs.append(FC(club_name))
	return(club_name)

