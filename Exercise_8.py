#Make a two-player Rock-Paper-Scissors game
# Driver program
def read_players():
	player1=input("Player1 Enter Rock-Paper-Scissors :")
	player2=input("Player2 Enter Rock-Paper-Scissors :")
	return player1 , player2
def RPS_game(player1,player2):
	while(player1=='Rock'):
		if player2=='Paper':
			print("player2 wins as paper beats rock")
			break
		elif player2=='Scissors':
			print("player1 wins as rock beats scissors")
			break
		else:
			print("Try again its a tie")
			break
	while(player1=='Paper'):
		if player2=='Rock':
			print("player1 wins as paper beats rock")
			break
		elif player2=='Scissors':
			print("player2 wins as scissors beats paper")
			break
		else:
			print("Try again its a tie")
			break
	while(player1=='Scissors'):
		if player2=='Rock':
			print("player2 wins as rock beats Scissors")
			break
		elif player2=='Paper':
			print("player1 wins as scissors beats paper")
			break
		else:
			print("Try again its a tie")
			break		
#print(RPS_game(player1,player2))
opt=' '
while opt!="quit":
	player1,player2=read_players()
	print(RPS_game(player1,player2))
	opt=input("enter quit to stop, or any key to continue to play :")
print("thank you for playing")

		
		
