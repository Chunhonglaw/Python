# Référence
# https://www.youtube.com/watch?v=731LoaZCUjo&feature=youtu.be
# wwww.pygame.org

import random
from player import Enemy

class Game:
    def __init__(self, speed=5, score=0, max_enemies=10, delay=0.1):
        self.speed = speed
        self.score = score
        self.max_enemies = max_enemies
        self.delay = delay

        self.enemy_list = []
    
    def drop_enemies(self, screen_width):
        delay = random.random()
        if len(self.enemy_list) < self.max_enemies and delay < self.delay:         # spawn with delay
            random_x = random.randint(0,screen_width)
            y_pos = 0
            enemy=Enemy(random_x,y_pos)
            self.enemy_list.append(enemy)

    def update_enemy_positions(self, screen_height):
        new_enemy_list = []
        for enemy in self.enemy_list:    
            if enemy.y >= 0 and enemy.y < screen_height:
                enemy.y += self.speed
                new_enemy_list.append(enemy)
            else:
                self.score += 1  
        self.enemy_list = new_enemy_list

    def set_level(self):
        if self.score < 20:
            self.speed = 5
        elif self.score < 30:
            self.speed = 10
        elif self.score < 60:
            self.speed = 15
        else:
            self.speed =30
    
    def collision_check(self, player):
        for enemy in self.enemy_list:
            if enemy.detect_collision(player):
                return True
        return False