import pygame
import time
import random

# Inicializar pygame
pygame.init()

# Definir colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Tamaño de la pantalla
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Tamaño del bloque de la serpiente y velocidad
block_size = 20
snake_speed = 15

# Fuentes personalizadas (Times New Roman)
game_over_font = pygame.font.SysFont("timesnewroman", 50, bold=True)  # Fuente grande para "Game Over!"
message_font = pygame.font.SysFont("timesnewroman", 25)  # Fuente más pequeña para el mensaje
score_font = pygame.font.SysFont("comicsansms", 35)  # Fuente para el puntaje

# Función para mostrar el puntaje
def show_score(score):
    value = score_font.render(f"Score: {score}", True, black)
    screen.blit(value, [10, 10])

# Función para dibujar la serpiente
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

# Función para mostrar mensajes en dos líneas centradas
def game_over_message():
    # Mensaje "Game Over!"
    game_over_text = game_over_font.render("Game Over!", True, red)
    game_over_rect = game_over_text.get_rect(center=(width // 2, height // 2 - 30))
    screen.blit(game_over_text, game_over_rect)
    
    # Mensaje "Press Q to exit or C to play again"
    message_text = message_font.render("Press Q to exit or C to play again", True, black)
    message_rect = message_text.get_rect(center=(width // 2, height // 2 + 20))
    screen.blit(message_text, message_rect)

# Función principal del juego
def gameLoop():
    game_over = False
    game_close = False

    # Posición inicial de la serpiente
    x1 = width / 2
    y1 = height / 2

    # Cambio de posición (movimiento)
    x1_change = 0
    y1_change = 0

    # Lista para el cuerpo de la serpiente
    snake_list = []
    length_of_snake = 1

    # Posición de la comida
    foodx = round(random.randrange(0, width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_over:

        while game_close:
            screen.fill(white)
            game_over_message()  # Mostrar mensaje de Game Over en dos líneas
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = block_size
                    x1_change = 0

        # Si la serpiente choca con los bordes
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(white)
        pygame.draw.rect(screen, red, [foodx, foody, block_size, block_size])
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Si la serpiente choca consigo misma
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        show_score(length_of_snake - 1)

        pygame.display.update()

        # Si la serpiente come la comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, height - block_size) / block_size) * block_size
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Iniciar el juego
gameLoop()
