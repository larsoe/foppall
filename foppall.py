#python3

import random


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

for ea in cities:
	print(ea, FC_ending[random.randrange(0,len(FC_ending))])
