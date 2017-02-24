def printMenu():
	print(".: Menu :.")
	print("1 - Get number of players")
	print("2 - Show all players")
	print("3 - Search Auction")
	print("4 - Give contracts to all players in squad")

def getAllPlayersInClub(fut):
	print(">> Getting all players in club...")
	fetch_size = 100
	players = []

	while True:
		players_fetched = fut.club(fetch_size, 10, 1, len(players))

		players += players_fetched

		if len(players_fetched) != fetch_size:
			break

	return players


import fut


print(">> Logando...")
fut = fut.Core('ale-remo@hotmail.com', 'ZOVHHWILale15', 'Belem','xbox', '123141')
print('>> Logado!')

while True:
	printMenu()

	choice = input('>> Option: ')

	if choice == "1":
		print(len(getAllPlayersInClub(fut)))
	elif choice == "2":
		players = getAllPlayersInClub(fut)

		for player in players:
			print(player)
			print(str(player['resourceId']) + " | " + str(player['discardValue']))

	elif choice == "3":
		assetId = input(">> Asset ID: ")

		auctions = fut.searchAuctions('development', defId="157960")

		print(auctions)

	elif choice == "4":
		squads = fut.squads()

		print("\n.: SQUADS :.\n")

		for squad in squads['squad']:
			print("-- {} | {} | {}".format(squad['squadName'], squad['rating'], squad['id']))

		squad_choice = int(input(">> Squad ID: "))

		squad_data = fut.squad(squad_choice)

		for player in squad_data[:12]:
			while player['contract'] < 10:
				player['contract'] += 1
				fut.applyPlayerContract(player['id'])

				print("# Contrato dado para {}".format(player['id']))


