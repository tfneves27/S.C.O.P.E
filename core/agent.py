from config.settings import COLOR_AGENT, AGENT_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH, AGENT_ENERGY, ENERGY_LOSS, BASAL_LOSS, COLOR_ENERGY_ATTENTION, COLOR_ENERGY_CRITICAL, COLOR_ENERGY_SAFE
import pygame, math

### Classe "Agent"
class Agent:
    ### Define as características do "Agent e onde ele irá nascer
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = COLOR_AGENT
        self.energy = AGENT_ENERGY
        self.vel = AGENT_SPEED
        self.basal_loss = BASAL_LOSS

    ### Método Draw
    def draw(self, screen):
        ### Criação da tela
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

        ### Cálculo para visualizar o gasto de energia de cada Agent
        current_width = (self.energy / 100) * 30
        if self.energy >= 50:
            color_to_draw = COLOR_ENERGY_SAFE
        elif self.energy >= 20:
            color_to_draw = COLOR_ENERGY_ATTENTION
        else:
            color_to_draw = COLOR_ENERGY_CRITICAL

        pygame.draw.rect(screen, color_to_draw, (self.x - 15, self.y - 20, current_width, 5))

    ### Método Update 
    def update(self, output):
        ### Gasto basal
        self.energy -= self.basal_loss

        ### Atualiza aa posição do Agent no mapa
        moved = False
        if output[0] > 0.5:
            self.y -= self.vel
            moved = True
        if output[1] > 0.5:
            self.y += self.vel
            moved = True
        if output[2] > 0.5:
            self.x -= self.vel
            moved = True
        if output[3] > 0.5:
            self.x += self.vel
            moved = True

        if moved:
            self.energy -= 0.1 
        self.check_walls()
    
    ### Método Check Wall
    def check_walls(self):
        if self.x < 0: self.x = 0
        if self.x > 800: self.x = 800
        if self.y < 0: self.y = 0
        if self.y > 600: self.y = 600

    ### Método get_data
    def get_data(self):
        ### Transforma a posição do Agent em distâncias reais até as bordas da tela 
        left = self.x
        right = SCREEN_WIDTH - self.x
        top = self.y
        base = SCREEN_HEIGHT - self.y
        return [left, right, top, base]
    
    # Método get_vision
    def get_vision(self, plants):
        ### Loop para identificar a planta mais próxima e definir o caminho até ela
        closest_dist = 10000
        closest_plant = None

        self.angle_to_plant = 0

        for p in plants:
            d = math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

            if d < closest_dist:
                closest_dist = d
                closest_plant = p

                dx = p.x - self.x
                dy = p.y - self.y

                self.angle_to_plant = math.atan2(dy, dx)
            if closest_plant is None:
                return 10000, 0 
            else:
                return closest_dist, self.angle_to_plant