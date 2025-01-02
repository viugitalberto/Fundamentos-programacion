import pygame
import random
import sys
from enum import Enum
from pygame import Surface
pygame.init()

screen_width = 600
screen_height = 600
game_objects_list=[]
list_gameobjects=[]
width=600
height=600
screen = pygame.display.set_mode((width,height))
font = pygame.font.Font(None, 36)



#Class
class GameObject:

    #constructor
    def __init__(self,tag,screen,pos_x=0,pos_y=0,image="fallenangel.png",visible=True):
        

        #Atributos de la instancia
        self.tag = tag
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = image
        
        #Atributos privados
        self.__img = pygame.image.load(self.image)
        self.__img.convert()
        self.__rect = self.__img.get_rect()
        self.__rect.center = pos_x, pos_y
        self.__screen = screen

    #Mover hacia arriba el gameobject
    def move_up(self,y=5):
        if (self.__rect.top-y) > 0:
            self.__rect.move_ip(0,-y)

    #Mover hacia derecha el gameobject
    def move_right(self,x=5):
        if self.__rect.right+x<self.__screen.get_width():
            self.__rect.move_ip(x,0)

    #Mover hacia izquierda el gameobject
    def move_left(self,x=5):
        if self.__rect.left - x > 0:
            self.__rect.move_ip(-x,0)

    #Mover hacia abajo el gameobject
    def move_down(self,y=5):
        if self.__rect.bottom + y < self.__screen.get_height():
            self.__rect.move_ip(0,y)

    #Funcion que devuelve la imagen del game_object
    def get_image(self):
        return self.__img
    
    #Funcion que actualiza la imagen del game_object
    def set_image(self,img):
        
        if isinstance(img, Surface):
           self.__img = img
        elif isinstance(img, str):
            self.__img = pygame.image.load(img).convert_alpha()
    
    #Funcion que devuelve el cuadrado del game_object
    def get_rect(self):
        return self.__rect

#Class Character
class Character(GameObject):
    # constructor
    def __init__(self, tag, screen, pos_x=0, pos_y=0,image="ghost.png",life=3,keychain="empty",alive=True, daño=False):
        super().__init__(tag, screen, pos_x, pos_y, image)

        #Atributos
        self.life=life #Los puntos de vida
        self.keychain=keychain #El llavero
        self.backpack=[] #La mochila o inventario
        self.alive=alive #Vivo o no vivo
        self.daño=daño #Para controlar si esta recibiendo daño
    # Cambia el estado de recibiendo daño de False a True
    def hurt(self):
        self.daño =True
    # Cambia el estado de recibiendo daño de True a False
    def nohurt(self):
        self.daño =False
    # Funcion que comprueba las colisiones        
    def __comprobar_colision(self,list_gameobjects):

     #Debo excluir de la comprobación al jugador que está en la posición 0
     for id in list_gameobjects:
        if id is not self and id.get_rect().colliderect(self.get_rect()):

        #Logica para el ghost
            if id.tag =="ghost":
                
                self.hurt() # Cambia el estado daño a True
                #Si tenemos weapon en la mochila 
                if weapon in player.backpack:
                    id.alive = False # El ghost muere
                    list_gameobjects.remove(id) # Lo borro de la lista de objetos
                  
                else:
                    
                    if player.life:
                        self.life-=1
                        print (self.life)
                        
                        
                    if player.life==0:
                        player.alive=False
                    
                return True       
                   
                
                  
        #Logica para la key
            if id.tag == "key":
                self.keychain="key"
                id.use()      
                list_gameobjects.remove(id)
                return True    
              
        #Logica para la potion
            if id.tag == "potion":
                self.backpack.append(potion)
                id.use()      
                list_gameobjects.remove(id)
                return True         
                 
        #Logica para el weapon
            if id.tag == "weapon":
                self.backpack.append(weapon)
                list_gameobjects.remove(weapon)
                return True

            #Colision de la door_exit:
            if id.tag=="door_exit" and self.keychain=="key":
                 id.open_door()
                 salida_alcanzada()
                 player.alive = False
                 print(f"Puerta de salida alcanzada")
                 return True
            if id.tag=="door_exit":     
                 return True   
        

             #Logica para las rocas y la puerta de entrada:
            if id.image=="rock.png" or id.tag=="door_entrance":
                 
                 return True  
                            
             
            else:
                return False
            
  

        
    def move_character_right(self, game_objects_list, x=5):
        super().move_right(x)
        if self.__comprobar_colision(game_objects_list):
                if self.daño:
                    super().move_left(50)
                elif self.__comprobar_colision(game_objects_list):
                    super().move_left(x)   

    def move_character_left(self, game_objects_list, x=5):
        super().move_left(x)
        if self.__comprobar_colision(game_objects_list):
            if self.daño:
                super().move_right(50)
            else:
                super().move_right(x) 

    def move_character_up(self, game_objects_list, y=5):
        super().move_up(y)
        if self.__comprobar_colision(game_objects_list):
            if self.daño:
                super().move_down(50)
            else:
                super().move_down(y) 


    def move_character_down(self, game_objects_list, y=5):
        super().move_down(y)
        if self.__comprobar_colision(game_objects_list):
            if self.daño:
                super().move_up(50)
            else:
                super().move_up(y) 

        
# Class Obstacle
# Atributo
# - hurt
class TypeObstacle(Enum):
    FURNITURE = 0
    TRAP = 1

class AmountDamage(Enum):
    LIGHT = 0
    HIGH = 1


        
class Obstacle(GameObject):
    def __init__(self, tag, screen, pos_x=0, pos_y=0, image="rock.png", type_obstacle=TypeObstacle.FURNITURE):
        super().__init__(tag, screen, pos_x, pos_y, image)

        #Estrutura o condicional ternario
        #self.__hurt = 0 if type_obstacle == TypeObstacle.FURNITURE else 1
        if type_obstacle == TypeObstacle.TRAP :
            self.__damage = AmountDamage.HIGH
        else:
            self.__damage  = AmountDamage.LIGHT

#Class Door
class Door(GameObject):
    def __init__(self, tag, screen, pos_x=0, pos_y=0, image="door_closed.png",open=False,exit_way=False):
        super().__init__(tag, screen, pos_x, pos_y, image)
        self.exit_way=exit_way
    def open_door(self):
         self.open=True  
    def close_door(self):
         self.open=False       
               
        
#Class Key
class Key(GameObject):
    def __init__(self, tag, screen, pos_x=0, pos_y=0, image="key.png", used=False,):
        super().__init__(tag, screen, pos_x, pos_y, image)
        self.used=True
        
    def use(self):
        self.used=True
        door_exit.open_door()
        
        

#Class Potion
class Potion(GameObject):
    def __init__(self, tag, screen, pos_x=0, pos_y=0, image="potion.png", used=False,points_life=1):
        super().__init__(tag, screen, pos_x, pos_y, image)
        self.used=used
        self.points_life=points_life
    def use(self):
        self.used=True
        
#Class Weapon
class Weapon(GameObject):
    def __init__(self, tag, screen, pos_x=0, pos_y=0, image="weapon.png", used=False):
        super().__init__(tag, screen, pos_x, pos_y, image)
        self.used=used
     
        
        

#Hacemos la puerta de entrada
door_entrance = Door(f"door_entrance", screen, random.randint(65, width-200),pos_y= random.randint(150, 500),image="door_opened.png",open=True)
    #Comprobar si el nuevo GameObject colsiona con TODOS los anteriores
for id in range(len(game_objects_list)):
        #Comprobamos la colisión entre door_entrance y el id
    if(game_objects_list[id].get_rect().colliderect(door_entrance.get_rect())):
            door_entrance = Door(f"door_entrance", screen,pos_x= random.randint(65, width -200),pos_y=random.randint(150, 500),)
                            
    id_door_entrance = 0
game_objects_list.append(door_entrance)#Lo añado a la lista     

#Creo la puerta de salida
door_exit = Door(f"door_exit", screen, random.randint(65, width-15), random.randint(30, height-15),image="door_closed.png",exit_way=True)
    #Comprobar si el nuevo GameObject colisiona con TODOS los anteriores
for id in range(len(game_objects_list)):
     #Comprobamos la colisión entre door_exit y el id
    if(game_objects_list[id].get_rect().colliderect(door_exit.get_rect())):
        door_exit = Door(f"door_exit", screen, random.randint(65, width - 15), random.randint(30, height - 15))
                            
    id_door_exit = 0
game_objects_list.append(door_exit)#Lo añado a la lista

#Creo el player
player = Character(f"player", screen,pos_x=door_entrance.get_rect().x+50,pos_y=door_entrance.get_rect().y, image="player.png")
for id in range(len(game_objects_list)):
        #Comprobamos la colisión entre el player y el id
    if(game_objects_list[id].get_rect().colliderect(player.get_rect())):
            player = Character(f"player", screen,pos_x=door_entrance.get_rect().x-25,pos_y=door_entrance.get_rect().y, image="player.png")
                            
    id_door_entrance = 0
game_objects_list.append(player)#Lo añado a la lista 

#Creo la potion
potion = Potion(f"potion", screen,pos_x= random.randint(15, width - 15),pos_y= random.randint(15, height - 15))

    #Comprobar si el nuevo GameObject colisiona con TODOS los anteriores
for id in range(len(game_objects_list)):
        #Comprobamos la colisión entre potion y el id
    if(game_objects_list[id].get_rect().colliderect(potion.get_rect())):
            potion = Potion(f"potion", screen,pos_x= random.randint(65, width - 15),pos_y= random.randint(30, height - 15),)
                            
    id_potion = 0
game_objects_list.append(potion)#Lo añado a la lista

#Creo el weapon
weapon = Weapon(f"weapon", screen,random.randint(65, width - 15),random.randint(30, height - 15))
#Comprobar si el nuevo GameObject colsiona con TODOS los anteriores
for id in range(len(game_objects_list)):
        #Comprobamos la colisión entre weapon y el id
    if(game_objects_list[id].get_rect().colliderect(weapon.get_rect())):
            weapon = Weapon(f"weapon",screen,pos_x= random.randint(65, width - 15),pos_y= random.randint(30, height - 15),)

game_objects_list.append(weapon)#Lo añado a la lista
      
#Hacemos la key
key = Key(f"key", screen, random.randint(65, width-15), random.randint(30, height-15))
    #Comprobar si el nuevo GameObject colsiona con TODOS los anteriores
for id in range(len(game_objects_list)):
        #Comprobamos la colisión entre key y el id
        if(game_objects_list[id].get_rect().colliderect(key.get_rect())):
            key = Key(f"key", screen, random.randint(65, width - 15), random.randint(30, height - 15))
                            
            id_key = 0
    
game_objects_list.append(key)#Lo añado a la lista

#Anyadir un numero de rocas
num_rocks = 5

for id_rock in range(num_rocks):
    rock = Obstacle(f"rock{id_rock}", screen, random.randint(65, width-15), random.randint(30, height-15), "rock.png")
    #Comprobar si el nuevo GameObject colisiona con TODOS los anteriores
    for id in range(len(game_objects_list)):
        #Comprobamos la colisión entre rock y el id
        if(game_objects_list[id].get_rect().colliderect(rock.get_rect())):
            rock = Obstacle(f"rock{id_rock}", screen, random.randint(65, width - 15), random.randint(30, height - 15),
                            "rock.png")
            id_rock = 0
   
    game_objects_list.append(rock)#Lo añado a la lista

################################################################################################################
#Creo al ghost (el enemigo) comprobando que no co##############################################################
for ghost in range(1):
    ghost = Character(f"ghost", screen,random.randint(65, width - 15),random.randint(30, height - 15), image="ghost.png")
   
    for id in range(len(game_objects_list)):
        
        if(game_objects_list[id].get_rect().colliderect(ghost.get_rect())):
            ghost = Character(f"ghost",screen,pos_x= random.randint(65, width - 15),pos_y= random.randint(30, height - 15),)

    game_objects_list.append(ghost)#Lo añado a la lista        
################################################################################################################
    ################################################################################################################
################################################################################################################

# Este numero indica el numero de vidas
number=GameObject(f"number", screen,pos_x= 37,pos_y = 16, image="3.png")
game_objects_list.append(number)
        
# Este es el corazon que aparece al lado del numero de vidas
heart=GameObject(f"heart0", screen,pos_x= 15,pos_y = 15, image="cajitablanca.png")
game_objects_list.append(heart)

#Funcion que muestra el mensaje de Game over al morir
def game_over():
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    text_rect = game_over_text.get_rect(center=(screen_width//2, screen_height//2))
    screen.fill((0, 0, 0))
    screen.blit(game_over_text, text_rect)
    pygame.display.flip()

    # Esperar un tiempo antes de cerrar el juego
    pygame.time.delay(2000)  

#Esta funcion enseña el mensaje "Puerta de salida alcanzada"
def salida_alcanzada():
    game_over_text = font.render("Puerta de salida alcanzada", True, (255, 0, 0))
    text_rect = game_over_text.get_rect(center=(screen_width//2, screen_height//2))
    screen.fill((0, 0, 0))
    screen.blit(game_over_text, text_rect)
    pygame.display.flip()

    # Esperar un tiempo antes de cerrar el juego
    pygame.time.delay(2000)      