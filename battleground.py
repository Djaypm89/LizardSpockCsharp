# The code below was created by Daniel Tulpa and revised using paired programming with partner John Mulln. 

import random
import time
from player import Player
from ai import AI
from human import Human
from fight import Fight
from type_speed import Type_Speed
type_this = Type_Speed
MEDIUM = 90
SLOW = 60
sleep = time.sleep(1.0)

class Battleground:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def welcome(self):
        type_this.slow_type('Welcome to RPSLS!', MEDIUM)
        type_this.slow_type('.....', 15)
        self.display_rules()
    
    def display_rules(self):
        type_this.slow_type('Like rock,paper,scissors this game will allow the user to select a gesture to use against their opponent.', 90)
        time.sleep(1.5)
        type_this.slow_type('This game varies from that standard a bit and adds two extra gestures: lizards and Spock', MEDIUM)
        time.sleep(1.5)
        type_this.slow_type('Rock crushes Scissors', SLOW)
        type_this.slow_type('Scissors cuts Paper', SLOW)
        type_this.slow_type('Paper covers Rock', SLOW)
        type_this.slow_type('Rock crushes Lizard', SLOW)
        type_this.slow_type('Lizard poisons Spock', SLOW)
        type_this.slow_type('Spock smashes Scissors', SLOW)
        type_this.slow_type('Scissors decapitates Lizard', SLOW)
        type_this.slow_type('Lizard eats Paper', SLOW)
        type_this.slow_type('Paper disproves Spock', SLOW)
        type_this.slow_type('Spock vaporizes Rock', SLOW)
        self.game_type()
        
    def game_type(self):
        type_this.slow_type('Enter "1" to play against a person. Enter "2" to play against a bot', MEDIUM)    
        game_type = int(input())
        if game_type == 1:
            self.player_two = Human()
        elif game_type == 2:
            self.player_two = AI()
        else:
            type_this.slow_type('Invalid input. Please try again',MEDIUM)
            self.game_type()
        self.battle()

    def battle(self):
        while self.player_one.number_of_wins < 2 and self.player_two.number_of_wins < 2:
            lets_fight = Fight()
            player1_choice = self.player_one.get_choice()
            player2_choice = self.player_two.get_choice()
            lets_fight.compare(self.player_one, self.player_two, player1_choice,player2_choice)
        self.display_winner()

    def display_winner(self):
        if self.player_one.number_of_wins == 2:
            type_this.slow_type('Congratulations, player 1, you won!', SLOW)
        else:
            type_this.slow_type('Congratulations, player 2, you won!',SLOW)
        self.restart()

    def restart(self):
        type_this.slow_type('Would you like to play another game? Type 1 to play again, type 2 to end',SLOW)
        restart_input = int(input())
        if restart_input == 1:
            restart = Battleground()
            restart.game_type()
        elif restart_input == 2:
            type_this.slow_type('Thank you for playing!', SLOW)
        else:
            type_this.slow_type('.....',15)
            type_this.slow_type('dude',40)
            time.sleep(2)
            type_this.slow_type('you had two options',40)
            time.sleep(1)
            type_this.slow_type('.....',15)
            type_this.slow_type('now...',40)
            type_this.slow_type('lets try this again',40)
            self.restart()
           




    #game rounds - repeat until one player has two points(while loop)
    #player one chooses a gesture
    #-prompt user to enter gesture
    #- save choice
    #-player two chooses gesture
    #compare choices
    #-winner gets a point
    #-no point if round is tie

    #end game
    #display winner

    #battleground.py
    #properties
    #-player_one = Human()
    #-player_two = none

# * Rock crushes Scissors
# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock