# Caitlyn Rogers
# CSCI 1200
# Lab Exercise 7.0
# 9/29/2021
 
#***********************************************************************
print('Lab 7.0')
print()

# Welcome the player to Rock Paper scissors 
player1 = input("Player 1, Please type your name: ")
print()
player2 = input("Player 2, Please type your name: ")
print()
print(f"Welcome to Rock, Paper, Scissors {player1.title()} and {player2.title()}!")
print()

# Prompt Player 1 for their selection and store it in a variable

choices = ['Rock', 'Paper', 'Scissors']

while True:
	player1_choice = input(f"{player1.title()}, please choose rock, paper, or scissors: ")
	if player1_choice.title() in choices:
			print("Thank you!")
			break
	if player1_choice.title() not in choices:
			print("Invalid input. Please choose rock, paper, or scissors")
	
print()

# Prompt Player 2 for their selection and store it in a variable
while True:
	player2_choice = input(f"{player2.title()}, please choose rock, paper, or scissors: ")
	if player2_choice.title() in choices:
			print("Thank you!")
			break
	if player2_choice.title() not in choices:
			print("Invalid input. Please choose rock, paper, or scissors")
			
print()


# Implement the if/elif/else chain. Try to refine it using nesting. 
    
if (player1_choice.title() == 'Rock'):
	if (player2_choice.title() == 'Scissors'):
		print(f"{player1.title()} Wins!")
	if (player2_choice.title() == 'Paper'):
		print(f"{player2.title()} Wins!")
	else:
		print("It's a Tie!")
elif (player1_choice.title() == 'Paper'):
	if (player2_choice.title() == 'Scissors'):
		print(f"{player2.title()} Wins!")
	if(player2_choice.title() == 'Rock'):
		print(f"{player1.title()} Wins!")
	else:
		print("It's a Tie!")
elif (player1_choice.title() == 'Scissors'):
	if (player2_choice.title() == 'Rock'):
		print(f"{player2.title()} Wins!")
	if (player2_choice.title() == 'Paper'):
		    print(f"{player1.title()} Wins!")


		
	



#***********************************************************************
print()
print('*****')
print()
print('End Lab 7.0')
