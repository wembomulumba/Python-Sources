superbowl_wins = [

['1', 'Pittsburgh', '6'],
['2', 'Dallas', '5'],
['3', 'Paris', '16'],
['4', 'Wembo CLub', '25'],

]

for row in superbowl_wins:
	print (row[1] + " had " + row[2] + " wins")

print("========================")

for row in superbowl_wins:
	for el in row:
		print (el)
		print('')
    		
