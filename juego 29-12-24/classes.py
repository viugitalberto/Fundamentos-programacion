import pygame
import random
import sys
from enum import Enum
from pygame import Surface

game_objects_list=[]
list_gameobjects=[]
width=600
height=600
screen = pygame.display.set_mode((width,height))




#Clase GameObject
#   Atributos
#   - tag
#   - pos_x
#   - pos_y
#   - image
#
#   Metodo
#   - get_image: Devuelve una image de pygame para ese gameobject
#   - get_rect: Devuelve el rectangulo que ocupa este gameobject
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
        else:
            print("Animal!!!!")
    

    #Funcion que devuelve el cuadrado del game_object
    def get_rect(self):
        return self.__rect


#Class Character
class Character(GameObject):
    # constructor
    def __init__(self, tag, screen, pos_x=0, pos_y=0, image="player.png",life=3,keychain="empty"):
        super().__init__(tag, screen, pos_x, pos_y, image)

        #Atributos
        self.__life=life
        self.keychain=keychain
        self.backpack=[]
    #Perseguir
    def perseguir_en_x(self, player):
        if enemy.pos_x < player.pos_x:
             enemy.move_character_right(game_objects_list) 
       
        
        else: 
           pass

    def __comprobar_colision(self,list_gameobjects):
  
     #Debo excluir de la comprobación al jugador que está en la posición 0
        #WARNING con el tema de la posicion 0
     for id in list_gameobjects:
        if id is not self and id.get_rect().colliderect(self.get_rect()):
                 
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
                 print(f"Puerta de salida alcanzada")
                 return True
            if id.tag=="door_exit":     
                 return True   
        

             #Logica para las rocas y la puerta de entrada:
            if id.image=="rock.png" or id.tag=="door_entrance":
                 print(self.backpack)
                 return True  
                            
             
            else:
                return False
        
    def move_character_right(self, game_objects_list, x=5):
        super().move_right(x)
        if self.__comprobar_colision(game_objects_list):
            super().move_left(x)

    def move_character_left(self, game_objects_list, x=5):
        super().move_left(x)
        if self.__comprobar_colision(game_objects_list):
            super().move_right(x)

    def move_character_up(self, game_objects_list, y=5):
        super().move_up(y)
        if self.__comprobar_colision(game_objects_list):
            super().move_down(y)

    def move_character_down(self, game_objects_list, y=5):
        super().move_down(y)
        if self.__comprobar_colision(game_objects_list):
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
    def __init__(self, tag, screen, pos_x=0, pos_y=0, image="potion.png", used=False,points_life=5):
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
     
        
 #####################################       
#Hacemos la puerta de entrada
door_entrance = Door(f"door_entrance", screen, random.randint(15, width-15), random.randint(15, height-15),image="door_opened.png",open=True)
    #Comprobar si el nuevo GameObject colsiona con TODOS los anteriores
for id in range(len(game_objects_list)):
        #Comprobamos la colisión entre key el id
    if(game_objects_list[id].get_rect().colliderect(door_entrance.get_rect())):
            door_entrance = Door(f"door_entrance", screen,pos_x= random.randint(15, width - 15),pos_y= random.randint(15, height - 15),)
                            
    id_door_entrance = 0
game_objects_list.append(door_entrance)#Lo añado a la lista     

#Creo la puerta de salida
door_exit = Door(f"door_exit", screen, random.randint(15, width-15), random.randint(15, height-15),image="door_closed.png",exit_way=True)
#Comprobar si el nuevo GameObject colsiona con TODOS los anteriores
for id in range(len(game_objects_list)):
    #Comprobamos la colisión
    if(game_objects_list[id].get_rect().colliderect(door_exit.get_rect())):
        door_exit = Door(f"door_exit", screen, random.randint(15, width - 15), random.randint(15, height - 15))
                            
    id_door_exit = 0
game_objects_list.append(door_exit)#Lo añado a la lista

#Creo el player
player=Character("player",screen,width/2,height/2,)
game_objects_list.append(player)#Lo añado a la lista


#Creo la potion
potion = Potion(f"potion", screen,pos_x= random.randint(15, width - 15),pos_y= random.randint(15, height - 15))

    #Comprobar si el nuevo GameObject colsiona con TODOS los anteriores
for id in range(len(game_objects_list)):
        #Comprobamos la colisión entre key el id
    if(game_objects_list[id].get_rect().colliderect(potion.get_rect())):
            potion = Potion(f"potion", screen,pos_x= random.randint(15, width - 15),pos_y= random.randint(15, height - 15),)
                            
    id_potion = 0
game_objects_list.append(potion)#Lo añado a la lista

#Creo el weapon
weapon = Weapon(f"weapon", screen,random.randint(15, width - 15),random.randint(15, height - 15))
#Comprobar si el nuevo GameObject colsiona con TODOS los anteriores
for id in range(len(game_objects_list)):
        #Comprobamos la colisión entre key el id
    if(game_objects_list[id].get_rect().colliderect(weapon.get_rect())):
            weapon = Weapon(f"weapon",screen,pos_x= random.randint(15, width - 15),pos_y= random.randint(15, height - 15),)

game_objects_list.append(weapon)
      

#Hacemos la key
key = Key(f"key", screen, random.randint(15, width-15), random.randint(15, height-15))
    #Comprobar si el nuevo GameObject colsiona con TODOS los anteriores
for id in range(len(game_objects_list)):
        #Comprobamos la colisión entre keyy el id
        if(game_objects_list[id].get_rect().colliderect(key.get_rect())):
            key = Key(f"key", screen, random.randint(15, width - 15), random.randint(15, height - 15))
                            
            id_key = 0
    #El nuevo objeto no colisiona
game_objects_list.append(key)

#Anyadir un numero de rocas
num_rocks = 4

for id_rock in range(num_rocks):
    rock = Obstacle(f"rock{id_rock}", screen, random.randint(15, width-15), random.randint(15, height-15), "rock.png")
    #Comprobar si el nuevo GameObject colsiona con TODOS los anteriores
    for id in range(len(game_objects_list)):
        #Comprobamos la colisión entre rock y el id
        if(game_objects_list[id].get_rect().colliderect(rock.get_rect())):
            rock = Obstacle(f"rock{id_rock}", screen, random.randint(15, width - 15), random.randint(15, height - 15),
                            "rock.png")
            id_rock = 0
    #El nuevo objeto no colisiona
    game_objects_list.append(rock)

#Creo al enemy
for id_enemy in range(1):
    enemy = Character(f"enemy", screen,random.randint(15, width - 15),random.randint(15, height - 15), image="enemy.png")


        #Comprobar si el nuevo GameObject colsiona con TODOS los anteriores
    for id in range(len(game_objects_list)):
        #Comprobamos la colisión entre key el id
        if(game_objects_list[id].get_rect().colliderect(enemy.get_rect())):
            enemy = Character(f"enemy",screen,pos_x= random.randint(15, width - 15),pos_y= random.randint(15, height - 15),)

    game_objects_list.append(enemy)

