import random

def play_again():
  play_again = input("Do you want to play again? Y/n ")
  if play_again == "Y":
    game()
  else:
    return print("OK, bye!")

def game():
  guesses = []
  try:
      secret_num = int(input("Pick a number between 1 and 10: "))
  except ValueError:
    print("{} is not a number. Try again.".format(guess))
  else:
    while len(guesses) < 5:
      computer_guess = random.randint(1, 10)
      
      # compare guess to secret number
      if computer_guess == secret_num:
        print("Hit! Number was {}".format(secret_num))
        break
      else:
        if computer_guess > secret_num:
          print("Too low!")
        else:
          print("Too high!")
      guesses.append(computer_guess)
    else:
      print("You're out of guesses! Number was {}.".format(secret_num))

  play_again()

game()