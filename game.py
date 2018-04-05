def play():
	inventory = ['Dagger','Gold(5)','Crusty Bread']

	print("Caspian")

	while True:
		action_input = get_player_command()

		if action_input in ['n','N']:
			print("You move north")

		elif action_input in ['s','S']:
			print("You move south")
		
		elif action_input in ['e','E']:
			print("You move east")

		elif action_input in ['w','W']:
			print("You move west")

		elif action_input in ['i','I']:
			print("Inventory:")
			for item in inventory:
				print('*' + str(item))

		else:
			print("Invalid Action")

def get_player_command():
	return input('Action: ')

play()
