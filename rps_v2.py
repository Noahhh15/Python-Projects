import random

def rockpaperscissors():

    rps_list = ["rock", "paper", "scissors"]

    c = (str(input("Rock, Paper, or Scissors? ")))
    ai = random.choice(rps_list)

    m = [c, ai]