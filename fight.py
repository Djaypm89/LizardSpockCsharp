# The code below was created by John Mullin and revised using paired programming with partner Daniel Tulpa. 
# 

import random
from player import Player 
from type_speed import Type_Speed
type_this = Type_Speed 
MEDIUM = 80

class Fight:
    def __init__(self):
        # pass
        from battleground import Battleground
        

    def compare(self,player1,player2,player_one_move, player_two_move):    
                user_choice = player_one_move
                ai_choice = player_two_move
                if user_choice == "rock":
                    if ai_choice == "rock":
                        type_this.slow_type("rock vs. rock, you tied!", MEDIUM)

                    elif ai_choice =="paper":
                        player2.number_of_wins += 1
                        type_this.slow_type("paper covers rock, player 2 wins.", MEDIUM)
                        

                    elif ai_choice == "scissors":
                        type_this.slow_type("rock smashes scissors, player 1 wins!", MEDIUM)
                        player1.number_of_wins += 1

                    elif ai_choice == "lizard":
                        type_this.slow_type("rock smashes lizard, player 1 wins! ", MEDIUM)
                        player1.number_of_wins += 1

                    elif ai_choice == "spock":
                        type_this.slow_type("spock vaporizes rock, player 2 wins.", MEDIUM)
                        player2.number_of_wins += 1


                elif user_choice == "paper":
                    if ai_choice == "rock":
                        type_this.slow_type("paper covers rock, player 1 wins!", MEDIUM)
                        player1.number_of_wins += 1

                    elif ai_choice =="paper":
                        type_this.slow_type("paper vs. paper, you tied!", MEDIUM)
                        
                    elif ai_choice == "scissors":
                        type_this.slow_type("scissors cuts paper, player 2 wins.", MEDIUM)
                        player2.number_of_wins += 1

                    elif ai_choice == "lizard":
                        type_this.slow_type("lizard eats paper, player 2 wins.", MEDIUM)
                        player2.number_of_wins += 1

                    elif ai_choice == "spock":
                        type_this.slow_type("paper disproves spock, player 1 wins!", MEDIUM)
                        player1.number_of_wins += 1
                    

                elif user_choice == "scissors":
                    if ai_choice == "rock":
                        type_this.slow_type("paper wraps rock, player 2 wins.", MEDIUM)
                        player2.number_of_wins += 1

                    elif ai_choice =="paper":
                        type_this.slow_type("scissors cuts paper, player 1 wins!", MEDIUM)
                        player1.number_of_wins += 1

                    elif ai_choice == "scissors":
                        type_this.slow_type("paper vs. paper, you tie!", MEDIUM)
                        
                    elif ai_choice == "lizard":
                        type_this.slow_type("scissors decapitates lizard, player 1 wins!", MEDIUM)
                        player1.number_of_wins += 1

                    elif ai_choice == "spock":
                        type_this.slow_type("spock smashes scissors, player 2 wins.", MEDIUM)
                        player2.number_of_wins += 1



                elif user_choice == "lizard":
                    if ai_choice == "rock":
                        type_this.slow_type("rock crushes lizard, player 2 wins.", MEDIUM)
                        player2.number_of_wins += 1

                    elif ai_choice =="paper":
                        type_this.slow_type("lizard eats paper, player 1 wins!", MEDIUM)
                        player1.number_of_wins += 1

                    elif ai_choice == "scissors":
                        type_this.slow_type("scissors decapitates lizard, player 2 wins.", MEDIUM)
                        player2.number_of_wins += 1
                        
                    elif ai_choice == "lizard":
                        type_this.slow_type("lizard vs lizard, you tie.", MEDIUM)
                        
                    elif ai_choice == "spock":
                        type_this.slow_type("lizard poisons spock, player 1 wins!", MEDIUM)
                        player1.number_of_wins += 1
                

                elif user_choice == "spock":
                    if ai_choice == "rock":
                        type_this.slow_type("spock vaporizes rock, player 2 wins.", MEDIUM)
                        player2.number_of_wins += 1

                    elif ai_choice =="paper":
                        type_this.slow_type("paper disproves spock, player 2 wins.", MEDIUM)
                        player2.number_of_wins += 1

                    elif ai_choice == "scissors":
                        type_this.slow_type("spock smashes scissors, player 1 wins!", MEDIUM)
                        player1.number_of_wins += 1
                        
                    elif ai_choice == "lizard":
                        type_this.slow_type("lizard poisons spock, player 2 wins.", MEDIUM)
                        player2.number_of_wins += 1

                    elif ai_choice == "spock":
                        type_this.slow_type("spock vs. spock, you tie", MEDIUM)
                        

                    