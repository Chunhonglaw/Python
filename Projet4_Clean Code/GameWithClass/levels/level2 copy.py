# Référence https://www.youtube.com/watch?v=731LoaZCUjo&feature=youtu.be
import sys
sys.path.insert(0, '../') #tell the system to go 1 directory higher
import pygame
from player import HumanPlayer


from screen import Screen
from game import Game
from main import play_game

if __name__ == "__main__":
    pygame.init()
    screen = Screen()
    player = HumanPlayer(screen.width/2, screen.height-100)
    game = Game()

    play_game(screen, player, game)