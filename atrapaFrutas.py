import pygame
import sys
import random
import time

pygame.init()

def main_game_loop():
    # Inicializar Pygame
    pygame.init()
    # Definir la variable de cierre
    start_game = False
    # Definir colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    #Definir puntaje
    puntos=0
    vidas=5
    # Configuración de la ventana de juego
    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Ventana de Juego")

    # Coordenadas del rectángulo
    rect_x = 350
    rect_y = 500
    rect_width = 100
    rect_height = 50
    rect_speed = 1

    # Lista de frutas que caen
    fruits = []

    class Fruit:
        def __init__(self):
            self.x = random.randint(0, window_size[0] - 30)
            self.y = 0
            self.speed = random.uniform(0.2, 0.5)

        def move(self):
            self.y += self.speed

        def draw(self):
            pygame.draw.circle(screen, (255, 0, 0), (self.x, int(self.y)), 15)

    # Control de tiempo para la frecuencia de aparición de objetos
    last_fruit_time = time.time()

    # Loop principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rect_x -= rect_speed
        if keys[pygame.K_RIGHT]:
            rect_x += rect_speed
        if rect_x > 860:
            rect_x = -50
        if rect_x < -60:
            rect_x = 850

        # Mover y eliminar frutas
        for fruit in fruits:
            fruit.move()
            if fruit.y > window_size[1]:
                fruits.remove(fruit)
                vidas-=1
                print(vidas)
            elif (rect_x < fruit.x < rect_x + rect_width and rect_y < fruit.y < rect_y + rect_height):
                # Colisión con el bloque, elimina la fruta
                fruits.remove(fruit)
                puntos+=1
                print(puntos)

        # Generar una nueva fruta cada 2 segundos
        current_time = time.time()
        if current_time - last_fruit_time >= 2.0:
            fruits.append(Fruit())
            last_fruit_time = current_time

        screen.fill(BLACK)
        pygame.draw.rect(screen, (240, 240, 240), (670, 30, 100, 50))
        pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))

        for fruit in fruits:
            fruit.draw()

        pygame.display.flip()

        # Comprobar clic en los botones
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if 770 >= mouse_x >= 670 and 80 >= mouse_y >= 50:
                start_game = True  # Esto indica que el juego debe iniciar

        if start_game:
            # Salir del bucle del juego y permitir iniciar el menu
            break

    # Salir del juego
    pygame.quit()

    if start_game:
        from menu import main_game_loo
        main_game_loo()

main_game_loop()
