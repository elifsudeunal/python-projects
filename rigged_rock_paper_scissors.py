import random

def generate_comp_choi():
    n = random.randint(1, 3)
    if n == 1:
        return "rock"
    elif n == 2:
        return "paper"
    else:
        return "scissors"
    
def generate_rigged_comp_choi(user_choi):
    if user_choi == "rock":
        return "paper"
    elif user_choi == "paper":
        return "scissors"
    else:
        return "rock"
    
score_user = 0
score_comp = 0

while True:
    user_choi = input("rock? paper? scissors? ").lower() #user choice
    if user_choi not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
        continue
    n = random.randint(1, 2)
    if n == 1:
        comp_choi = generate_comp_choi() #computer choice
    else:
        comp_choi = generate_rigged_comp_choi(user_choi)
    print("Computer:", comp_choi)

    if comp_choi == user_choi:
        print("Draw")
    elif comp_choi == "rock" and user_choi == "paper":
        score_user += 1
    elif comp_choi == "paper" and user_choi == "scissors":
        score_user += 1
    elif comp_choi == "scissors" and user_choi == "rock":
        score_user += 1
    else:
        score_comp += 1
    
    print("You:", score_user, "VS Computer:", score_comp)

    if score_user == 3 or score_comp == 3:
        break

if score_comp > score_user:
    print("YOU LOST :( ")
else:
    print("YOU WON :) ")