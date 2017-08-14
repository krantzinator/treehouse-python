import random

def play_again():
  play_again = input("Do you want to play again? Y/n ")
  if play_again == "Y":
    game()
  else:
    return print("OK, bye!")

def game():
  # generate random number 1-10
  secret_num = random.randint(1, 10)
  guesses = []
  
  while len(guesses) < 5:
    # get number guess from player
    try:
      guess = int(input("Guess a number between 1 and 10: "))
    except ValueError:
      print("{} is not a number. Try again.".format(guess))
    else:
      # compare guess to secret number
      if guess == secret_num:
        print("Hit! Number was {}".format(secret_num))
        break
      else:
        if guess < secret_num:
          print("Too low!")
        else:
          print("Too high!")
    guesses.append(guess)
  else:
    print("You're out of guesses! Number was {}.".format(secret_num))

  play_again()

game()