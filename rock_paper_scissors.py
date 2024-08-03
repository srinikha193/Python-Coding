# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import random

def get_choices():
    player_choice=input("enter a choice:(rock,paper,scissors)")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices
def check_win(player,computer):
    print(f"you chose {player} computer chose {computer}")
    if player == computer:
        return "Its a tie!"
    elif player=="rock":
        if computer=="scissors":
            return "Rock smashes scissors!you win!"
        else:
            return "paper covers rock! you lose!"
    elif player=="paper":
        if computer=="rock":
            return "paper covers rock! you win!"
        else:
            return "scissors cut paper! you lose!"
    elif player=="scissors":
        if computer=="rock":
            return "Rock smashes scissors!you lose!"
        else:
            return "scissors cut paper! you win!"    
        
choice=get_choices()
print(check_win(choice["player"],choice["computer"]))


