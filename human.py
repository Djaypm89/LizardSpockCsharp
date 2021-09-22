# The code below was created using paired programming, by Daniel Tupla and John Mullin. 

from player import Player
from type_speed import Type_Speed
type_this = Type_Speed

class Human(Player):
    def __init__(self):
        super().__init__()
    

    def get_choice(self):
        type_this.slow_type("Choose rock, paper, scissors, lizard or spock: ", 90)
        user_choice = input()  # change user_choice to player_choice?
        if user_choice in ["Rock", "rock"]:
            user_choice = "rock"
        elif user_choice in ["Paper", "paper"]:
            user_choice = "paper"
        elif user_choice in ["scissors", "scissors"]:
            user_choice = "scissors"
        elif user_choice in ["Lizard", "lizard"]:
            user_choice = "lizard"
        elif user_choice in ["Spock", "spock"]: 
            user_choice = "spock"
        else:
            print("not a valid choice, please choose rock, paper, scissors, lizard or spock: ")
            self.get_choice()
        # self.gesture_choice = user_choice
        return user_choice
    
    # need to display running total of wins, need game to break when winner reaches 2 out of 3 wins. 