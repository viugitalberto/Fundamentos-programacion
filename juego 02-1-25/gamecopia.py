#Importaciones
import pygame
from classescopia import game_objects_list,screen, dx, dy, player, ghost, potion, number, weapon, game_over

#Pygame inicializacion
pygame.init()
# Establezco la velocidad del ghost
velocidad_ghost = 3
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
        #Esta es la logica para el movimiento del enemigo
        dx = player.get_rect().x - ghost.get_rect().x
        dy = player.get_rect().y - ghost.get_rect().y
        #Si la distancia entre ghost y player es mayor en x que en y se mueve en x primero
        if abs(dx) > abs(dy):
        # Mueve el ghost en el eje x
            if dx >= 0:
                ghost.get_rect().x += velocidad_ghost
            else:
                ghost.get_rect().x -= velocidad_ghost
        else:
        # Mueve el ghost en el eje y
            if dy >= 0:
                ghost.get_rect().y += velocidad_ghost
            else:
                ghost.get_rect().y -= velocidad_ghost
    
        #Esta logica detecta cuanto pulsamos una tecla
        if event.type == pygame.KEYDOWN:
            
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
                #Detecta si hemos cogido el arma y cambia la image para mostrar al pj con el arma en la mano
                if weapon in player.backpack:
                    if player.image == "player.png":
                        player.set_image("playerwweapon.png") 
                # Control del FLIP de la imagen
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
                    
        #Si cerramos la ventana o el jugador muere el juego se acaba
        if event.type == pygame.QUIT:
            running = False 
        elif player.alive==False:
            game_over()
            running = False
            
        #Detecta cuando levantamos la tecla y para al pj
        if event.type == pygame.KEYUP:
            
            player_move = False
           
    
    #Este codigo cambia el número de vidas que se muestran arriba al lado del corazón:
    if player.life >3:
        number.set_image("4.png")
    elif player.life ==3:
        number.set_image("3.png")
    elif player.life ==2:
        number.set_image("2.png")
    elif player.life ==1:
        number.set_image("1.png")    
    # El codigo que controla el movimiento del personaje
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
    #Me aseguro de que el daño de player este en False
    player.nohurt()
    #Pintamos los objectos
    for game_object in game_objects_list:
        screen.blit(game_object.get_image(),game_object.get_rect())   
    
    #Actualizo la pantalla
    pygame.display.flip()
    #Limito los FPS
    clock.tick(60)  

#Salir del bucle
pygame.quit()



        
