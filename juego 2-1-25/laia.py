import pygame
import sys

# Inicializa Pygame
pygame.init()

# Establece la resolución de la pantalla
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Establece los colores
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Establece las velocidades
velocidad_perseguidor = 2
velocidad_objeto = 2

# Establece las posiciones iniciales
x_perseguidor = screen_width / 2
y_perseguidor = screen_height / 2
x_objeto = screen_width / 4
y_objeto = screen_height / 4

# Establece la dirección del objeto
direccion_x_objeto = 1
direccion_y_objeto = 1

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mueve el objeto
    x_objeto += velocidad_objeto * direccion_x_objeto
    y_objeto += velocidad_objeto * direccion_y_objeto

    # Revisa si el objeto ha llegado al borde de la pantalla
    if x_objeto < 0 or x_objeto > screen_width:
        direccion_x_objeto *= -1
    if y_objeto < 0 or y_objeto > screen_height:
        direccion_y_objeto *= -1

    # Mueve el perseguidor
    dx = x_objeto - x_perseguidor
    dy = y_objeto - y_perseguidor
    distancia = (dx ** 2 + dy ** 2) ** 0.5
    if distancia > 0:
        x_perseguidor += dx / distancia * velocidad_perseguidor
        y_perseguidor += dy / distancia * velocidad_perseguidor

    # Dibuja la pantalla
    screen.fill(white)
    pygame.draw.rect(screen, red, (x_perseguidor, y_perseguidor, 20, 20))
    pygame.draw.rect(screen, blue, (x_objeto, y_objeto, 20, 20))
    pygame.display.flip()

    # Limita la velocidad a 60 FPS
    pygame.time.Clock().tick(60)