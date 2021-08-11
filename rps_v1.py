import random

rps_list = ["rock", "paper", 'scissors']

def rockpaperscissors():

    c = (str(input("Rock Paper or Scissors? ")))
    ai = random.choice(rps_list)

    if c == ai:
        print("You guys picked the same thing, it's a draw. ")
    
    if c == "rock" and ai == "paper":
        print("You lost, paper beats rock. ")
    elif c == "rock" and ai == "scissors":
        print("You won, rock beats paper. ")
    if c == "paper" and ai == "scissors":
        print("You lost, scissors beats paper. ")
    elif c == "paper" and ai == "rock":
        print("You won, paper beats rock. ")
    if c == "scissors" and ai == "rock":
        print("You lost, rock beats scissors. ")
    elif c == "scissors" and ai == "paper":
        print("You won, scissors beats paper. ")
    
    r = (str(input("Hit Enter to play again, or type and hit enter to quit. ")))
    print(r)

    if r == "":
        rockpaperscissors()
    else:
        pass

rockpaperscissors()