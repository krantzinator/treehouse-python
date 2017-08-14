import os
import sys
import random

# make a list of words
words = [
  'matzo',
  'yogurt',
  'banana',
  'cornchips',
  'almonds',
  'salmon',
  'beef',
  'pork',
  'onion',
  'noino'
]

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
    
def draw(bad_guesses, good_guesses, word):
  clear()

  print("Strikes: {}/7".format(len(bad_guesses)))
  print('')
  
  for letter in bad_guesses:
    print(letter, end='')
  print('\n\n')

  for letter in word:
    if letter in good_guesses:
      print(letter, end='')
    else:
      print('_', end='')

  print('')

def make_a_guess(bad_guesses, good_guesses):
  while True:
    guess = input("Guess a letter: ").lower()
  
    if len(guess) != 1:
      print("You can only guess a single letter")
    elif guess in bad_guesses or guess in good_guesses:
      print("You've already guessed that letter")
    elif not guess.isalpha():
      print("You can only guess letters")
    else:
      return guess

def play(done):
  clear()
  word = random.choice(words)
  bad_guesses = []
  good_guesses = []
  
  while True:
    draw(bad_guesses, good_guesses, word)
    guess = make_a_guess(bad_guesses, good_guesses)
    
    if guess in word:
      good_guesses.append(guess)
      found = True
      for letter in word:
        if letter not in good_guesses:
          found = False
      if found:
        print("You win!")
        print("The secret word was '{}'".format(word))
        done = True
    else:
      bad_guesses.append(guess)
      if len(bad_guesses) == 7:
        draw(bad_guesses, good_guesses, word)
        print("You lost!")
        print("The secret word was '{}'".format(word))
        done = True
  
    if done:
      play_again = input("Play again? Y/n ").lower()
      if play_again != 'n':
        return play(done=False)
      else:
        sys.exit()

def welcome():
  start = input("Press enter/return to start, or Q to quit")
  if start == 'q':
    print("Bye!")
    sys.exit()
  else:
    return True

print("Welcome to da beestest game evahhh")

done = False

while True:
  clear()
  welcome()
  play(done)
