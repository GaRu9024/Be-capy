import pygame
import random
import time

# Inicializa Pygame
pygame.init()

def main_game_loop():
    # Configuración de la ventana
    WIDTH, HEIGHT = 800, 600  # Tamaño de la ventana
    WINDOW_SIZE = (WIDTH, HEIGHT)
    WINDOW = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Memorama")
    
    start_game = False
    # Colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Carga  las imágenes de las cartas 
    card_images = [pygame.image.load("imagenes/carta1.png"), pygame.image.load("imagenes/carta2.jpg"),
                   pygame.image.load("imagenes/carta3.png"), pygame.image.load("imagenes/carta4.jpg")]

    # Escala las imágenes al mismo tamaño
    card_width, card_height = 100, 150
    for i in range(len(card_images)):
        card_images[i] = pygame.transform.scale(card_images[i], (card_width, card_height))

    # Duplica las cartas para hacer pares
    cards = card_images * 2
    random.shuffle(cards)

    # Tamaño de la cuadrícula
    grid_width, grid_height = 4, 2

    # Espacio entre las cartas
    card_spacing_x, card_spacing_y = 10, 10

    # Calcula el tamaño de la cuadrícula y el espacio adicional
    grid_width_px = grid_width * (card_width + card_spacing_x) - card_spacing_x
    grid_height_px = grid_height * (card_height + card_spacing_y) - card_spacing_y

    # Centra la cuadrícula en la ventana
    start_x = (WIDTH - grid_width_px) // 2
    start_y = (HEIGHT - grid_height_px) // 2

    # Coordenadas de las cartas en la cuadrícula
    card_coords = []
    for x in range(grid_width):
        for y in range(grid_height):
            x_coord = start_x + x * (card_width + card_spacing_x)
            y_coord = start_y + y * (card_height + card_spacing_y)
            card_coords.append((x_coord, y_coord))

    # Otras variables
    flipped = []
    matched_pairs = []  # Lista de pares de cartas coincidentes
    font = pygame.font.Font(None, 36)

    # Tiempo para mostrar las cartas volteadas
    showing_time = 1  # en segundos
    showing_timer = None

    def draw_cards():
        for i, card in enumerate(cards):
            if i not in flipped and i not in [pair for sublist in matched_pairs for pair in sublist]:
                # Dibuja la carta boca abajo
                card_back = pygame.image.load("imagenes/carta.jpg")
                card_back = pygame.transform.scale(card_back, (card_width, card_height))
                x, y = card_coords[i]
                WINDOW.blit(card_back, (x, y))
            else:
                # Dibuja la carta boca arriba
                x, y = card_coords[i]
                WINDOW.blit(card, (x, y))

    def check_match():
        nonlocal matched_pairs, flipped, showing_timer
        if len(flipped) == 2:
            if cards[flipped[0]] == cards[flipped[1]]:
                matched_pairs.append(flipped[:])  # Agregar el par coincidente
                print("¡Match!")
                flipped = []  # Reiniciar las cartas volteadas
            else:
                # Mostrar las cartas durante un tiempo antes de voltearlas
                showing_timer = time.time() + showing_time

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if len(flipped) < 2 and showing_timer is None:  # Evitar voltear más de 2 cartas a la vez
                    x, y = event.pos
                    index = None
                    for i, (card_x, card_y) in enumerate(card_coords):
                        if card_x <= x < card_x + card_width and card_y <= y < card_y + card_height:
                            index = i
                            break
                    if index is not None and index not in [pair for sublist in matched_pairs for pair in sublist]:
                        flipped.append(index)
                        if len(flipped) == 2:
                            check_match()

        WINDOW.fill(WHITE)
        draw_cards()

        pygame.draw.rect(WINDOW, (240, 240, 240), (670, 30, 100, 50))
        
        # Verificar el temporizador de visualización
        if showing_timer is not None and time.time() > showing_timer:
            showing_timer = None
            for i in flipped[:]:
                if i not in [pair for sublist in matched_pairs for pair in sublist]:
                    flipped.remove(i)

        pygame.display.update()

        if len(matched_pairs) == len(cards) / 2:
            text = font.render("¡Has ganado!", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            WINDOW.blit(text, text_rect)
            pygame.display.update()
            time.sleep(2)
            running = False
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if 770 >= mouse_x >= 670 and 80 >= mouse_y >= 50:
                start_game = True  # Esto indica que el juego debe iniciar

        if start_game:
            # Salir del bucle del juego y permitir iniciar el menu
            break

    pygame.quit()
    if start_game:
        from menu import main_game_loo
        main_game_loo()

# Llama a la función principal
main_game_loop()
