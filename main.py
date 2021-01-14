import random
from art import rock, paper, scissors


# PROPERTIES
moves = [rock, paper, scissors]


# MAIN
print("Let's play Rock Paper Scissors")

game_is_in_progress = True

while game_is_in_progress:
  user_choice = int(input("Choose your move, 1 2 or 3: "))
  user_move = moves[user_choice - 1]
  opponent_move = random.choice(moves)

  print("You chose:")
  print(user_move)
  print("Your opponent chose:")
  print(opponent_move)

  ending_msg = ""

  if user_move == rock and opponent_move == scissors:
    ending_msg = "You win!"
  elif user_move == rock and opponent_move == paper:
    ending_msg = "You lose. Try again."
  elif user_move == paper and opponent_move == rock:
    ending_msg = "You win!"
  elif user_move == paper and opponent_move == scissors:
    ending_msg = "You lose. Try again."
  elif user_move == scissors and opponent_move == paper:
    ending_msg = "You win!"
  elif user_move == scissors and opponent_move == rock:
    ending_msg = "You lose. Try again."
  else:
    ending_msg = "You both chose the same move. It's a draw."

  print(ending_msg)

  user_answer = input("Would you like to play again? (y/n) ").lower()

  if user_answer != "y":
    print("Goodbye")
    game_is_in_progress = False
