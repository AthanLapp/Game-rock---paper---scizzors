import random
r=random.randint(1,3)
guess= input('rock,paper,scizzors')
if guess=='rock':
	guess = 1
elif guess == 'paper':
	guess = 2
else:
	guess = 3

if r == 1:
	print('computer chose rock')
elif r==2:
	print('computer chose paper')
else:
	print('computer chose scizzors')

if guess == r:
	print('draw')
if guess ==1 and r == 2:
	print('Computer wins')
if guess == 1 and r == 3:
	print('Player wins')
if guess == 2 and r == 1:
	print('Player wins')
if guess == 2 and r == 3:
	print('Computer wins')
if guess == 3 and r == 1:
	print('Computer wins')
if guess == 3 and r == 2:
	print('Player wins')

