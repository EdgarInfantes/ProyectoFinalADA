import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dibujar Línea con Clic Presionado")

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bucle principal
running = True
is_mouse_pressed = False
start_pos = None
end_pos = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botón izquierdo
                is_mouse_pressed = True
                start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_mouse_pressed = False
                end_pos = pygame.mouse.get_pos()

    screen.fill(WHITE)

    # Dibujar la línea si el clic izquierdo está presionado
    if is_mouse_pressed:
        end_pos = pygame.mouse.get_pos()
        pygame.draw.line(screen, BLACK, start_pos, end_pos, 2)

    pygame.display.flip()

# Salir del programa
pygame.quit()
sys.exit()
