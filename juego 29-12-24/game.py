#Importamos pygame
import pygame
import random
import sys
from classes import GameObject,  Obstacle, Door, game_objects_list, screen, width, height, player, enemy

#Pygame inicializacion
pygame.init()
#Definimos clock, lo usaremos para capar los fps
clock = pygame.time.Clock()

# Control del movimiento con tecla apretada
key_press=""
player_move=False
# Control del FLIP de la imagen
player_moving_left=False
player_moving_right=True
#El juego se ejecute de forma infinita
running = True

#El bucle del juegod
while running:
   # pygame.event PILA DE EVENTOS que ocurren en la ventana
    # get -> Dame el primer evento ocurrido
    for event in pygame.event.get():
        if enemy.pos_x < player.pos_x:
             enemy.move_character_right(game_objects_list)
        if event.type == pygame.KEYDOWN:
            #print("Tecla apretada")
            if event.unicode == "w":
                player.move_character_up(game_objects_list)
                key_press = "w"
                player_move = True
            elif event.unicode == "d":
                #Control del FLIP de la imagen
                player_moving_right = True
                if player_moving_left:
                    imgFlip=pygame.transform.flip(player.get_image(),True,False)
                    player_moving_left = False
                    player.set_image(imgFlip)
                # Control del FLIP de la imagen
                #player.move_right()
                player.move_character_right(game_objects_list)
                key_press = "d"
                player_move = True
            elif event.unicode == "a":
                # Control del FLIP de la imagen
                player_moving_left = True
                if player_moving_right:
                    imgFlip=pygame.transform.flip(player.get_image(),True,False)
                    player_moving_right = False
                    player.set_image(imgFlip)
                # Control del FLIP de la imagen
                player.move_character_left(game_objects_list)
                key_press = "a"
                player_move = True
            elif event.unicode == "s":
                player.move_character_down(game_objects_list)
                key_press = "s"
                player_move = True
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            #print("Tecla soltada")
            player_move = False

    #El código pasa por aquí como si no hubiera un mañana
    if player_move:
        if key_press == "w":
            player.move_character_up(game_objects_list,2)
        elif key_press == "d":
            player.move_character_right(game_objects_list,2)
        elif key_press == "a":
            player.move_character_left(game_objects_list, 2)
        elif key_press == "s":
            player.move_character_down(game_objects_list, 2)
    # fill the screen with a color to wipe away anything from last frame
    screen.fill([188,170,164])
    #Pintamos los objectos
    for game_object in game_objects_list:
        screen.blit(game_object.get_image(),game_object.get_rect())    
    # RENDER YOUR GAME HERE
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
  

pygame.quit()



