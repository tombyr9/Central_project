import pygame
import random
import sys
import os
from function import *
from jeux1bis import *
from quizz import *

m = 1000000
bag = []
shop = {"parc_dattraction" : 1000000, "aire_de_jeu" : 10000, "statue" : 1500, "magasin_de_fleurs": 200000, "caserne_douvriers": 3000, "petite_centrale" : 8000}

open
pygame.init() #Initialisation de la séance d'affichage

# Définition de la couleur blanche
blanc = (255, 255, 255) #Initialisation des couleurs blanches et noires
noir = (0, 0, 0)
#Tout ce qui a en dessous sont des initialisation du jeu de Tom
#################################################################################################
#Définition des deux classes utiles pour le jeu vidéo de Tom mini_game_thief
class character:
    def __init__(self):
        self.speed = 2
        self.life = 3
        self.y = 230
        self.x = 300
        self.taille = (25,25)
        self.position = (self.x, self.y)

class text:
    def __init__(self):
        self.speed = 2
        self.life = 3
        self.y = 270
        self.x = 220
        self.taille = (25,25)
        self.position = (self.x, self.y)
#Permet d'utiliser les classes et ses composantes du mini jeu de Tom mini_game_thief
thief = character()
text = text()
#Génère les images utiles au jeu vidéo de Tom, mini_game_thief
thief_image_0 = pygame.image.load("design/character_0.png")
thief_image_1 = pygame.image.load("design/character_1.png")
#Une liste qui sert à l'animation du personnage du jeu de Tom, mini_game_thied
thief_frames = [thief_image_0, thief_image_1]
#Un index qui sert à l'animation du personnage du jeu de Tom, mini_game_thied
index = 0
#Une liste de direction qui sert à l'animation du personnage du jeu de Tom, mini_game_thief
direction = ["up", "down", "left", "right"]
#Une police d'écriture de direction qui sert au texte du jeu de Tom, mini_game_thief
font = pygame.font.Font(None, 36)  # Utilise la police par défaut avec une taille de 36 points
font2 = pygame.font.Font(None, 66)
#Plusieurs fonctions qui servent au jeu de Tom, mini_game_thief
def thief_animation(thief_frames, thief , index):
    current_frame = pygame.transform.scale(thief_frames[int(index)], thief.taille)
    return current_frame

def thief_walk(current_frame, thief):
    screen.blit(current_frame, thief.position)

#Faire une foncton qui fait avancer le bonhomme dans une direction aléatoire
def change_position(thief):
    if choice == "up" and 0<thief.y<455 and 0<thief.x<640:
        thief.y += 1
    elif choice == "down" and 0<thief.y<455 and 0<thief.x<640:
        thief.y -= 1
    elif choice == "left" and 0<thief.x<640 and 0<thief.y<455:
        thief.x -= 1
    elif choice == "right" and 0<thief.x<640 and 0<thief.y<455:
        thief.x += 1
    print(choice)

play_button = pygame.image.load("design/play_button.png") #On initialise une variable avec l'image du bouton.
play_button_crop = pygame.transform.scale(play_button, (150,75)) #On rogne la taille de cette image du bouton.

# Création d'une surface de texte
texte_before_game_1 = font.render("Le voleur est sur le point de s'échapper !", True, noir)
texte_before_game_2 = font.render("Clique dessus avant qu'il ne s'enfuit.", True, noir)
texte_before_game_3 = font.render("Prêt ?", True, noir)
texte_restart = font.render("On recommence ?", True, noir)
texte_win = font2.render("Bravo ! Tu l'as attrapé !", True, blanc)
texte_win_rect = texte_win.get_rect()
texte_win_rect = texte_win_rect.move((85,230))
text_discover_map = font.render("Clique sur la carte pour l'actualiser.", True, blanc)
texte_thief_exit = font.render("Il s'est echappé !", True, noir)
# Faire apparaître du texte
touch = False

start = False
before_start = True
after_start = False
##################################################################
#Tout ce qui a au dessus sont des initialisation du jeu de Tom
crop = (640,455)
screen = pygame.display.set_mode((640, 455)) #L'écran affiché est de la taille 640 x 455
pygame.display.set_caption("CenTown") #Le titre de la fenêtre est "CenTown"

#Modifiable :
title = pygame.image.load("design/pixilart-drawing.png") #L'image jpg du logo est mis dans un format spécial dans la variable pygame. C'est le format "surface", nécessaire pour que pygame l'utilise.
image_rect = title.get_rect() #On met les coordonnées du titre dans une variable qu'on modifiera

background_1 = pygame.image.load("design/frame-1.gif") #On initialise trois variables background différentes qui vont être les frames de notre animation du menu.
background_2 = pygame.image.load("design/frame-2.gif")
background_3 = pygame.image.load("design/frame-3.gif")
background_index = 0 #On initialise un compteur qui servira plus tard mais il est pas nécessaire.
background_gif = [background_1, background_2, background_3]
for i in range(2):
    background_gif[i]= pygame.transform.scale(background_gif[i], crop)

city_map = pygame.image.load("design/city_map_grey.png") #On initialise une variable avec l'image de la ville.
city_map_crop = pygame.transform.scale(city_map, crop) #On rogne cette image dde la ville aux dimensions 640, 455

play_button = pygame.image.load("design/play_button.png") #On initialise une variable avec l'image du bouton.
play_button_crop = pygame.transform.scale(play_button, (150,75)) #On rogne la taille de cette image du bouton.
play_button_crop_rect = play_button_crop.get_rect() #On met la taille de la surface de ce bouton rogné, dans une variable
play_button_crop_rect = play_button_crop_rect.move((230,300)) #On déplace la surface du bouton au centre bas de l'écran

shop_image = pygame.image.load("design/shop_image.png")
shop_image_crop = pygame.transform.scale(shop_image, (200,220))
shop_image_crop_rect = shop_image_crop.get_rect()
shop_image_crop_rect = shop_image_crop_rect.move((460,230))

shop_button = pygame.image.load("design/shop_button.png")
shop_button_crop = pygame.transform.scale(shop_button, (100, 40))
shop_button_crop_rect = shop_button_crop.get_rect()
shop_button_crop_rect = shop_button_crop_rect.move((510,410))

wall_indoor_shop = pygame.image.load("design/wall_shop.jpg")
wall_indoor_shop_crop = pygame.transform.scale(wall_indoor_shop,(640, 455))

nuclear_central = pygame.image.load("design/nuclear_central.png")
nuclear_central_crop = pygame.transform.scale(nuclear_central, (230,150))

nuclear_central_button = pygame.image.load("design/Central_button.png")
nuclear_central_button_crop = pygame.transform.scale(nuclear_central_button, (100,75))

return_button = pygame.image.load("design/return_button.png")
return_button_crop = pygame.transform.scale(return_button, (80, 80))
return_button_crop_rect = return_button_crop.get_rect()
return_button_crop_rect = return_button_crop_rect.move((20,370))

child = pygame.image.load("design/child.png")
child_crop = pygame.transform.scale(child, (60,75))
child_crop_rect = child_crop.get_rect()
child_crop_rect = child_crop_rect.move((20,40))

library = pygame.image.load("design/library.jpg")
library_crop = pygame.transform.scale(library, (670,455))
library_crop_rect = library_crop.get_rect()
library_crop_rect = library_crop_rect.move((0,0))

chapitre1 = pygame.image.load("design/chapitre1.png")
chapitre1_crop = pygame.transform.scale(chapitre1, (180,105))
chapitre1_crop_rect = chapitre1_crop.get_rect()
chapitre1_crop_rect = chapitre1_crop_rect.move((240, 20))

chapitre2 = pygame.image.load("design/chapitre1.png")
chapitre2_crop = pygame.transform.scale(chapitre1, (180,105))
chapitre2_crop_rect = chapitre1_crop.get_rect()
chapitre2_crop_rect = chapitre1_crop_rect.move((240, 20))

chapitre2grey = pygame.image.load("design/chapitre2-grey.png")
chapitre2grey_crop = pygame.transform.scale(chapitre2grey, (180,105))
chapitre2grey_crop_rect = chapitre2grey_crop.get_rect()
chapitre2grey_crop_rect = chapitre2grey_crop_rect.move((240,100))

chapitre3grey = pygame.image.load("design/chapitre3-grey.png")
chapitre3grey_crop = pygame.transform.scale(chapitre3grey, (180,105))
chapitre3grey_crop_rect = chapitre3grey_crop.get_rect()
chapitre3grey_crop_rect = chapitre3grey_crop_rect.move((240, 180))

chapitre4grey = pygame.image.load("design/chapitre4-grey.png")
chapitre4grey_crop = pygame.transform.scale(chapitre4grey, (180,105))
chapitre4grey_crop_rect = chapitre4grey_crop.get_rect()
chapitre4grey_crop_rect = chapitre4grey_crop_rect.move((240,260))

chapitre5grey = pygame.image.load("design/chapitre5-grey.png")
chapitre5grey_crop = pygame.transform.scale(chapitre5grey, (180,105))
chapitre5grey_crop_rect = chapitre5grey_crop.get_rect()
chapitre5grey_crop_rect = chapitre5grey_crop_rect.move((240,340))

victoire = 0
cpt = 0
print_title = True #On initialise une booléenne. Lorsqu'elle sera fausse, on cessera d'afficher le titre.
print_background = True #Même chose pour le fond d'écran.
print_play_button = True #Même chose pour le bouton play
print_city_map_crop = False #Mêeme chose pour la map de la ville
print_shop = False
print_indoor_shop = False
print_nuclear_central_shop = False
print_nuclear_central_logo = False
print_return_button = False
print_child = False
mini_game_thief = False
mini_game_quizz =False
print_library = False
print_chapitre1 = False
print_chapitre2grey = False
print_chapitre3grey = False
print_chapitre4grey = False
print_chapitre5grey = False
aim_lab_charbon=False
resultat=False
police = pygame.font.SysFont(None, 48)


run = True
while run: #Tant que le programme est en cours
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Tant que la croix n'a pas été cliqué, le programme continue
                run = False
        #Instructions  qui s'éxecute après avoir touché à bouton
        if event.type == pygame.KEYDOWN: #Si la flèche du bas est saisie
            if event.key == pygame.K_DOWN and image_rect.y < 170:
                image_rect.y += 2 #L'ordonnée de l'image est modifiée, elle ne peut pas sortir de l'image grâce à la condition du dessus.
            if event.key == pygame.K_UP and image_rect.y > -90: #Si la flèche du haut est saisia
                image_rect.y -= 2 #Même chose que plus haut

        #Instruction d'appuyer sur un boutton
        if event.type == pygame.MOUSEBUTTONDOWN:

            if play_button_crop_rect.collidepoint(event.pos)and (mini_game_thief==False):#Lorsqu'on appuie sur le bouton entrée
                hub = open_town() #J'associe à une variable, les 5 qui sont retournées par la fonction "open town()", qui affiche uniquement les images qui sont nécessaire au menu de la ville : donc les images du shop, du fond d'écran et de l'enfant.
                print_play_button,print_title,print_city_map_crop,print_shop,print_child = hub #Je mets à jours les 5 variables, en leur donnant leur nouvelle valeur "true" ou "false" qui sont comprise dans "hub"

            if (shop_button_crop_rect.collidepoint(event.pos) and print_city_map_crop ==True) or (shop_image_crop_rect.collidepoint(event.pos) and print_city_map_crop==True) and (mini_game_thief==False): #Lorsqu'on appuie sur le bouton shop
                hub = close_town()
                print_city_map_crop, print_shop, print_child = hub
                shop = open_shop()#J'associe à une variable, les 5 qui sont retournées par la fonction "open town()", qui affiche uniquement les images qui sont nécessaire à la boutique
                print_indoor_shop, print_nuclear_central_shop, print_nuclear_central_logo, print_return_button = shop#Je mets à jours les 5 variables, en leur donnant leur nouvelle valeur "true" ou "false" qui sont comprise dans "shop".

            if return_button_crop_rect.collidepoint(event.pos) and (print_indoor_shop == True) and (mini_game_thief==False): #Si je suis dans le shop et que je clique sur le bouton return alors je reviens à l'affichage de la ville.
                hub = close_shop()
                print_indoor_shop, print_nuclear_central_shop, print_nuclear_central_logo, print_return_button = hub
                hub = open_town()
                print_play_button,print_title,print_city_map_crop,print_shop,print_child = hub

            if child_crop_rect.collidepoint(event.pos) and (print_city_map_crop == True):
                print_library = True
                print_return_button = True
                print_chapitre1 = True
                print_chapitre2grey = True
                print_chapitre3grey = True
                print_chapitre4grey = True
                print_chapitre5grey = True

            if chapitre1_crop_rect.collidepoint(event.pos) and (print_library == True):
                print_library = False
                print_chapitre1= False
                mini_game_thief = True
                print_return_button = False
                print_chapitre2grey = False
                print_chapitre3grey = False
                print_chapitre4grey = False
                print_chapitre5grey = False
            if chapitre2grey_crop_rect.collidepoint(event.pos) and (print_library == True):
                print_library = False
                print_chapitre1= False
                mini_game_thief = False
                print_return_button = False
                print_chapitre2grey = False
                print_chapitre3grey = False
                print_chapitre4grey = False
                print_chapitre5grey = False
                aim_lab_charbon=True

            if chapitre3grey_crop_rect.collidepoint(event.pos) and (print_library==True): #lilia
                print_library = False
                print_chapitre1 = False
                mini_game_thief = False
                print_return_button = False
                print_chapitre2grey = False
                print_chapitre3grey = False
                print_chapitre4grey = False
                print_chapitre5grey = False
                mini_game_quizz= True


            if return_button_crop_rect.collidepoint(event.pos) and (print_library == True) and (mini_game_thief==False): #Si je suis dans la librairie et que je clique sur le bouton return alors je reviens à l'affichage de la ville.
                print_library = False
                print_chapitre1 = False
                print_return_button = False
                print_chapitre2grey = False
                print_chapitre3grey = False
                print_chapitre4grey = False
                print_chapitre5grey = False





        #Instructions pour pour l'affichage d'une image
        if print_background == True: #tant qu'on met la variable à Vrai, on affiche le fond d'écran
            if background_index >2: #Une suite d'instructions qui font en sorte que les éléments du décor s'affichent avec une certaine latence.
                background_index = 0
            if background_index <=2:
                screen.blit(background_gif[int(background_index)],(0,0))
                background_index = background_index+0.015 #Plus la valeur additionnée sera basse, plus la transition sera lente.

        if print_city_map_crop == True:
            screen.blit(city_map_crop,(0,0))
        if print_shop == True:
            screen.blit(shop_image_crop, (460, 230))
            screen.blit(shop_button_crop, (510,410))
        if print_title == True: #Tant qu'on met la variable à Vrai, on affiche le titre
            screen.blit(title,(-20, image_rect.y))
        if print_play_button == True:
            screen.blit(play_button_crop,(230,300))
        if print_indoor_shop == True    :
            screen.blit(wall_indoor_shop_crop,(0,0))
        if print_nuclear_central_shop == True:
            screen.blit(nuclear_central_crop,(0,70))
        if print_nuclear_central_logo == True:
            screen.blit(nuclear_central_button_crop,(65,190))
        if print_child == True:
            screen.blit(child_crop,(20,40))
        if print_library==True:
            screen.blit(library_crop,(0,0))
        if print_chapitre1 == True:
            screen.blit(chapitre1_crop, (240, 20))
        if print_chapitre2grey == True:
            screen.blit(chapitre2grey_crop, (240, 100))
        if print_chapitre3grey == True:
            screen.blit(chapitre3grey_crop, (240, 180))
        if print_chapitre4grey == True:
            screen.blit(chapitre4grey_crop, (240, 260))
        if print_chapitre5grey == True:
            screen.blit(chapitre5grey_crop, (240, 340))
        if print_return_button == True:
            screen.blit(return_button_crop, (20, 350))
        if victoire == 1:
            if print_win_text == True:
                screen.blit(texte_win, (45,180))
                screen.blit(text_discover_map,(85,230))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if texte_win_rect.collidepoint(event.pos):
                    city_map = pygame.image.load("design/city_map_grey1.png")  # On initialise une variable avec l'image de la ville.
                    city_map_crop = pygame.transform.scale(city_map, crop)
                    print_win_text = False
        pygame.display.update() #Mise à jour
        # continue du programme
        if aim_lab_charbon==True:
            print_child = False
            print_shop = False
            print_background = False
            print_city_map_crop = False
            resultat=run_game()
            if resultat == True:
                print("jeu fini")
                victoire=2
                aim_lab_charbon=False
                screen = pygame.display.set_mode((640, 455))
                hub = open_town()
                print_play_button, print_title, print_city_map_crop, print_shop, print_child = hub
            else:
                hub = open_town()
                print_play_button, print_title, print_city_map_crop, print_shop, print_child = hub
                break

        if mini_game_thief == True:
            print_child = False
            print_shop = False
            print_background = False
            print_city_map_crop = False
            screen.fill(blanc)
            # L'animation du bonhomme
            index += 0.00001  # Incrémentez l'index
            index = index + 0.01
            if (index >= 2):
                index = 0
            if before_start == True:
                touch = False
                screen.blit(texte_before_game_1, (100, 90))
                screen.blit(texte_before_game_2, (110, 150))
                screen.blit(texte_before_game_3, (200, 360))
                screen.blit(play_button_crop, (300, 330))
                play_button_crop_rect = play_button_crop.get_rect()  # On met la taille de la surface de ce bouton rogné, dans une variable
                play_button_crop_rect = play_button_crop_rect.move((300, 330))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button_crop_rect.collidepoint(event.pos):  # Lorsqu'on appuie sur le bouton entrée
                        before_start = False
                        start = True
                thief.x, thief.y = 300, 230
                screen.blit(thief_animation(thief_frames, thief, index), (thief.x, thief.y))

            if start == True:
                # Un choix aléatoire est fait
                choice = random.choice(direction)

                if (thief.y <= 0) or (thief.y >= 455) or (640 <= thief.x) or (thief.x <= 0):
                    touch = True
                if touch == True:
                    screen.blit(texte_thief_exit, text.position)
                    screen.blit(texte_restart, (215, 300))
                    screen.blit(play_button_crop, (235, 340))
                    play_button_crop_rect = play_button_crop.get_rect()  # On met la taille de la surface de ce bouton rogné, dans une variable
                    play_button_crop_rect = play_button_crop_rect.move((225, 340))
                    if event.type == pygame.MOUSEBUTTONDOWN and touch == True:
                        if play_button_crop_rect.collidepoint(event.pos):  # Lorsqu'on appuie sur le bouton entrée
                            before_start = True
                            start = False
                # Lorsque le choix est fait thief.x et thief.y sont modifiés
                change_position(thief)
                # On met la surface du voleur dans une variable rect (obligatoire pour la collision future avec le curseur)
                current_frame_rect = thief_animation(thief_frames, thief,index).get_rect()  # On met la taille de la surface de ce bouton rogné, dans une variable
                # On veut que la surface se déplace aux mêmes positions que le voleur
                current_frame_rect = current_frame_rect.move(thief.x, thief.y)
                if event.type == pygame.MOUSEBUTTONDOWN and touch == False:
                    if current_frame_rect.collidepoint(event.pos):  # Lorsqu'on appuie sur le bouton entrée
                        before_start = False
                        start = False
                        after_start = True
                # Actualise l'affichage du voleur avec les nouvelles coordonnées et sa bonne frame d'animation
                screen.blit(thief_animation(thief_frames, thief, index), (thief.x, thief.y))
            if after_start == True: #Cette condition provoque l'arrêt de jeu et rammène à l'affichage de la ville. Comme after start reste True pour toujours, alors l'enfant ne pourra plus jamais refaire ce niveau.
                cpt +=1
                mini_game_thief = False
                if cpt == 1:
                    print_win_text = True
                victoire = 1
                hub = open_town()  # J'associe à une variable, les 5 qui sont retournées par la fonction "open town()", qui affiche uniquement les images qui sont nécessaire au menu de la ville : donc les images du shop, du fond d'écran et de l'enfant.
                print_play_button, print_title, print_city_map_crop, print_shop, print_child = hub


            # Rafraîchir l'affichage
        print(mini_game_quizz)

        if mini_game_quizz == True:
            print_child = False
            print_shop = False
            print_background = False
            print_city_map_crop = False

            show_start_screen()
            start_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 50)

            current_question=0
            score=0
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if start_button.collidepoint(mouse_pos):
                            while current_question < len(questions):
                                buttons = show_question(current_question)
                                pygame.display.flip()
                                waiting = True
                                while waiting:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            mouse_pos = pygame.mouse.get_pos()
                                            for i, button in enumerate(buttons):
                                                if button.collidepoint(mouse_pos):
                                                    waiting = False
                                                    if i == correct_choices[current_question]:
                                                        score += 1
                                                    current_question += 1
                                                    break
                            screen.blit(background, (0, 0))
                            draw_text("Votre score est : " + str(score) + "/" + str(len(questions)), font, BLACK,
                                      screen,
                                      WIDTH // 2, HEIGHT // 2)
                            pygame.display.flip()
                            pygame.time.wait(5000)
                            pygame.quit()
                            sys.exit()

                pygame.draw.rect(screen, BLACK, start_button)
                draw_text("Start", font, WHITE, screen, start_button.centerx, start_button.centery)

                pygame.display.flip()

# Remplir l'écran avec la couleur blanche

# Boucle principale du jeu



pygame.quit()
quit()
