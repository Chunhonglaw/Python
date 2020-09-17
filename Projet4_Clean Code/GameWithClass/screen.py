# Référence
# https://www.youtube.com/watch?v=731LoaZCUjo&feature=youtu.be
# wwww.pygame.org

from color import Color

class Screen:
    def __init__(self, width=800, height=600, background_color=Color.BLACK, font_type="nomospace", font_size=35, clock_tick=30):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.font_size = font_size
        self.screen = pygame.display.set_mode((width,height))
        self.font = pygame.font.SysFont(font_type, font_size)
        self.clock = pygame.time.Clock()
        self.clock.tick = clock_tick
        
    def refresh_background(self):
        self.screen.fill(sefl.background_color)
    
    def draw_enemies(self, enemy_list):
        for enemy in enemy_list:
            enemy.draw(self.screen)


    def draw_player(self, player):
        player.draw(self.screen)
    
    def draw_score_label(self, score, color=Color.YELLOW):
        #test = "Score:" + str(score)
        text = f"Score: {score}"
        label = self.font.render(text, 1, color)
        self.screen.blit(label, self.width=200, self.height=40())

    def update_screen(self, enemy_list,  player, score):
        self.refresh_background
        self.draw_enemies(enemy_list)
        self.draw_player(player)