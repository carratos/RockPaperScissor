'''
Rock Paper Scissor Game against the computer. User enters their choice of rock,
paper, or scissor and computer randomlychooses a response and result are output
to the console.
'''
from random import randint

print 'Welcome to Rock Paper Scissors'
print 'Select implement of choice:'
print '0) Rock'
print '1) Paper'
print '2) Scissors'
rpsList = ['Rock', 'Paper', 'Scissors']
#USer enters integer value which gets evaluated against rpsList
user = rpsList[int(raw_input('Enter Selection: '))]
#print 'You chose ' + str(userChoice)
comp = rpsList[randint(0, 2)]
print user + ' vs. ' + comp
if user == comp:
  print 'Tie!'
elif user == 'Rock':
  if comp == 'Scissors':
    print 'You win!'
  else:
    print 'You lose!'
elif user == 'Paper':
  if comp == 'Rock':
    print 'You win!'
  else:
    print 'You lose!'
else:
  if comp == 'Paper':
    print 'You win!'
  else:
    print 'You lose!'

print 'Thanks for Playing'
