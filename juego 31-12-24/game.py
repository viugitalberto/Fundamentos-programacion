#Importamos pygame
import pygame
import random
import math
import sys
from classes import GameObject,   Obstacle, Door, game_objects_list, screen, width, height, player, enemy, potion, heart, number



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

#################################################################################
#El bucle del juego
while running==True:
    
   # pygame.event PILA DE EVENTOS que ocurren en la ventana
    # get -> Dame el primer evento ocurrido
    for event in pygame.event.get():

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
            elif event.unicode == "p" and potion in player.backpack:
                    player.life += 1
                    player.backpack.remove(potion)
                    
        
        if event.type == pygame.QUIT or player.alive==False:
            running = False
        
        if event.type == pygame.KEYUP:
            #print("Tecla soltada")
            player_move = False
    
    
    #Me aseguro de que el daño de player este en False
    player.nohurt()
    #Este codigo cambia el número de vidas que se muestran arriba al lado del corazón:
    if player.life >3:
        number.set_image("4.png")
    elif player.life ==3:
        number.set_image("3.png")
    elif player.life ==2:
        number.set_image("2.png")
    elif player.life ==1:
        number.set_image("1.png")    
    # El codido que captura el movimiento del player:
    if player_move:
        if key_press == "w":
            player.move_character_up(game_objects_list,2)
        elif key_press == "d":
            player.move_character_right(game_objects_list,2)
        elif key_press == "a":
            player.move_character_left(game_objects_list, 2)
        elif key_press == "s":
            player.move_character_down(game_objects_list, 2)
    # Pinto el fondo:
    screen.fill([188,170,164])

    #Pintamos los objectos
    for game_object in game_objects_list:
        screen.blit(game_object.get_image(),game_object.get_rect())   
    
   
          
    #Actualizo la pantalla
    pygame.display.flip()
    clock.tick(60)  #Limita los FPS
   
  
#Sale del bucle
pygame.quit()



        
