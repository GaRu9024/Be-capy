import pygame
import sys
def main_game_loo():
    game_running1 = False  # Variable para controlar si el juego está en ejecución
    game_running2 = False  # Variable para controlar si el juego está en ejecución
    game_running3 = False  # Variable para controlar si el juego está en ejecución
    # Inicializar Pygame
    pygame.init()

    # Definir colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Configuración de la ventana principal
    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Menú del Juego")

    # Definir fuentes
    font = pygame.font.Font(None, 36)

    # Función para crear botones
    def draw_button(screen, text, x, y, width, height, color):
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x + width / 2, y + height / 2)
        screen.blit(text_surface, text_rect)

    # Loop principal del menú
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill(BLACK)
        draw_button(screen, "Botón 1", 300, 200, 200, 50, (0, 128, 0))
        draw_button(screen, "Botón 2", 300, 300, 200, 50, (0, 0, 128))
        draw_button(screen, "Botón 3", 300, 400, 200, 50, (128, 0, 0))

        pygame.display.flip()

        # Comprobar clic en los botones
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if 300 <= mouse_x <= 500 and 200 <= mouse_y <= 250:
                game_running1 = True
            if 300 <= mouse_x <= 500 and 300 <= mouse_y <= 350:
                game_running2 = True
                
        if game_running1 or game_running2:
        # Salir del bucle del menú y permitir iniciar el juego
            break
        
        
    # Salir del menú
    pygame.quit()

    # Iniciar el juego si game_running es True
    if game_running1:
        from atrapaFrutas import main_game_loop
        main_game_loop()
        print("hola")
          # Ejecutar el bucle principal del juego
    if game_running2:
        from memoria import main_games_loop
        main_games_loop()
        print("hola")
          # Ejecutar el bucle principal del juego


main_game_loo()
