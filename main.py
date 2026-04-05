from core.agent import Agent
from core.food import Food
from config.settings import SCREEN_HEIGHT, SCREEN_WIDTH, COLOR_BACKGROUND
import pygame, sys, random, math

pygame.init()

# Controle de tempo do "robô"
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("Arial", 20, bold=True)

# Objeto "Robô"
robot = Agent(640, 360)

# Criação do objeto "Plants"
plants = []


robots = []
for i in range(30):
    rx = random.randint(50, SCREEN_WIDTH - 50)
    ry = random.randint(50, SCREEN_HEIGHT - 50)
    robots.append(Agent(rx, ry))

# Criação de múltiplos objetos "Plants"
for i in range(6):
    random_x = random.randint(0, SCREEN_WIDTH)
    random_y = random.randint(0, SCREEN_HEIGHT)
    plants.append(Food(random_x, random_y))

# Objeto "Generation"
generation = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(COLOR_BACKGROUND)

    # Texto da Geração
    txt_gen = font.render(f"GENERATION: {generation}", True, (255, 255, 255))
    screen.blit(txt_gen, (20, 50))
    
    # Texto da População
    txt_pop = font.render(f"PPOPULATION: {len(robots)}", True, (255, 255, 255))
    screen.blit(txt_pop, (20, 80))

    # Keys
    keys = pygame.key.get_pressed()
    robot.update(keys)
    
    robots_to_keep = []

    for r in robots:
        r.get_vision(plants)
        r.update(keys)
        
        foods_to_maintain = []

        for p in plants:
            dist = math.sqrt((r.x - p.x)**2 + (r.y - p.y)**2)
            if dist < 15:
                r.energy += 15
                new_x = random.randint(50, SCREEN_WIDTH - 50)
                new_y = random.randint(50, SCREEN_HEIGHT - 50)
                foods_to_maintain.append(Food(new_x, new_y))
            else:
                foods_to_maintain.append(p)
        
        plants = foods_to_maintain

        if r.energy > 0:
            robots_to_keep.append(r)

    robots = robots_to_keep
    
    if len(robots) == 0:
        generation += 1 

        for i in range(30):
            rx = random.randint(50, SCREEN_WIDTH - 50)
            ry = random.randint(50, SCREEN_HEIGHT - 50)
            robots.append(Agent(rx, ry))

    # Criação dos objetos "Food"
    for p in plants:
        p.draw(screen)
        
    # Criação da lista para manter as "Plants"
    foods_to_maintain = []

    dados = robot.get_data()
    print(dados)
    
    # Criação dos objetos "Robot"
    for r in robots:
        r.draw(screen)

    pygame.display.flip()

    # Relógio funcionando
    clock.tick(60)