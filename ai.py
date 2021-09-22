# # The code below was created using paired programming, by Daniel Tupla and John Mullin. 

from player import Player
import random
from type_speed import Type_Speed
type_this = Type_Speed

class AI(Player):
    def __init__(self):
        super().__init__()

    def get_choice(self):
        ai_choice = random.randint(1,5)          
        if ai_choice == 1:
            ai_choice = "rock"
        elif ai_choice == 2:
            ai_choice = "scissors"
        elif ai_choice == 3:
            ai_choice = "paper"
        elif ai_choice == 4:
            ai_choice = "lizard"
        else:                               
            ai_choice = "spock"

        type_this.slow_type(f'The bot has chosen {ai_choice}',60)

        return ai_choice