# Snake Water Gun


# Importing random

import random


# Defining Snake Water and Gun

powers = ["Snake", "Water", "Gun"]


# Defining variables

turns = 10

computer = "Computer : "
player = input("Entre your name : ").capitalize()

computer_point = 0
player_point = 0


# Defining functions

def choices() : # Takes your and computer choice
	
	global player_choice, computer_choice
	
	computer_choice = random.choice(powers)
	player_choice = input(f"{player} : I choose - ")
	

def win() : # When you win a turn
	
	global player_point
	
	print(f"{your_choice} > {computer_choice} so, you got +1 point\n")
	
	player_point += 1
	

def lost() : # When you lost a turn
	
	global computer_point
	
	print(f"{computer_choice} > {your_choice} so, you got -1 point\n")
	
	computer_point += 1
	
		
def draw() : # When a turn goes draw
	
	print(f"{your_choice} = {computer_choice} so, nobody gets the point\n")	
	

# Starter Guide

print (f"\n\n{computer} Welcome to Snake Water Gun program, press - \n\n S for Snake \n W for Water \n G for gun \n\n")
	

# Main code starts from here

while(turns > 0) :
	

	turns -= 1
	
	
	choices()
	
	

# When you choose 🐍
	
	if player_choice.capitalize() == "S" :
		
		your_choice = "Snake"
		
		
		if computer_choice == "Snake" : draw()
		
		elif computer_choice == "Water" : win()
		
		elif computer_choice == "Gun" : lost()
		
		

# When you choose 💦
	
	elif player_choice.capitalize() == "W" :
		
		your_choice = "Water"
		
		
		if computer_choice == "Snake" : lost()
		
		elif computer_choice == "Water" : draw()
		
		elif computer_choice == "Gun" : win()
		
		
	
# When you choose 🔫

	elif player_choice.capitalize() == "G" :
		
		your_choice = "Gun"
		
		
		if computer_choice == "Snake" : win()
		
		elif computer_choice == "Water" : lost()
		
		elif computer_choice == "Gun" : draw()
		
		
		
	else :
		
		print("Invalid input! Only s, w and g are accepted here\n")
		
		turns += 1
		
		
	
# Declaration of the whole match results

if computer_point > player_point :
	
	print(f"{computer} Sorry! you have lost by {computer_point - player_point} point ")
	

elif player_point > computer_point :
	
	print(f"{player} : Yeh! I have victory over you by {player_point - computer_point} point ")
	

else :
	
	print("The match has resulted draw")