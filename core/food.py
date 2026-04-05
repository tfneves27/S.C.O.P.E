from config.settings import COLOR_FOOD
import pygame

### Classe Food
class Food:
    ### Define a identidade da planta
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = COLOR_FOOD
        self.radius = 5

    ### Desenha as plantas na tela
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)