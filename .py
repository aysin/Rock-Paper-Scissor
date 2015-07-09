#Rock-Paper-Scissor Game

import sys
from random import randint

rock = 'r'
paper = 'p'
scissor = 's'
choices = [rock, paper, scissor]

comp_score = user_score = 0

def user_move():
	move = raw_input("Enter your choice ('r', 'p', 's', 'q')\n>").lower()

	if move in choices:
		return move
	elif move == 'q':
		print "I hope enjoy the game"
		sys.exit(0)
	else:
		print "invalid entry. Try again."
		 

def comp_move():
	return choices.__getitem__(randint(0,2))

def score():
	print "Wins: {}, Loses: {}".format(user_score, comp_score)

def comp_win():
	global comp_score
	comp_score += 1

def user_win():
	global user_score
	user_score += 1

def winner(user, comp):
	if user == comp: 
		print "Its a tie."
	elif user == rock and comp == paper:
		print "Paper wraps the rock. Computer Wins"
		comp_win()
	elif user == paper and comp == rock:
		print "Paper wraps the rock. User Wins"
		user_win()
	elif user == scissor and comp == rock:
		print "Rock smashed the scissor. Computer Wins"
		comp_win()
	elif user == rock and comp == scissor:
		print "Rock smashed the scissor. User Wins"
		user_win()
	elif user == paper and comp == scissor:
		print "Scissor cuts the paper. Computer Wins!"
		comp_win()
	elif user == scissor and comp == paper:
		print "Scissor cuts the paper. User Wins!"
		user_win()


def main():
	print "Starting the Rock-Paper-Scissor Game."
	turns = 0


	while True:
		user = user_move()
		comp = comp_move()

		while user_move is 'invalid':
			print "Enter a valif move (r,p,s)"
			user = user_move()

		winner(user, comp)
		score()

		if turns == 0:
			print "Make another move or press q to quit."
		turns += 1

main()


