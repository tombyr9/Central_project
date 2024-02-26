import pygame
import os

def open_the_shop(shop): #Fonction pour ouvrir le magasin
    print("Bienvenu dans la boutique. Voici les infrastructures disponibles.")
    for key in shop.keys():
        print(key,":",shop[key]," dollars.")

def see_the_wallet(wallet): #Fonction pour ouvrir le portemonnaie
    print("Vous avez", wallet, "dollars dans votre portemonnaie.")

def buy_in_the_shop(shop, bag, wallet): #Fonction pour acheter dans le shop
    T = []
    i = 1
    for value in shop: #J'affiche les infrastructures et les nombres à saisir pour les ajouter au sac.
        print(value,":" ,i, end=" ||| ")
        T.append(value) #Je mets les infrastructures dans une liste mais au premier terme plutôt qu'au ième terme.
        i+=1
    x = int(input("\nSaisir l'objet à acheter :")) #L'utilisateur donne le chiffre associé pour que le programme retrouve l'infrastructure dans la liste.
    if shop[T[x-1]] <= wallet: #Vérifie que la valeur de l'insfrastructure qui lui est associé dans le dico "shop" soit inférieur à la somme dans le portmonnaie.
        bag.append(T[x-1]) #Le terme i = 1 est à la place 0 du tableau, donc pareil pour tous les autres, incrémentation de -1.
    wallet = wallet-shop[T[x-1]]

def print_bag(bag): #Fonction qui affiche ce qu'il y a dans le sac de l'utilisateur.
    print("Vous possédez dans votre sac :", bag)

wallet = 1000000
bag = []
shop = {"parc_dattraction" : 1000000, "aire_de_jeu" : 10000, "statue" : 1500, "magasin_de_fleurs": 200000, "caserne_douvriers": 3000, "petite_centrale" : 8000}

open
pygame.init() #Initialisation de la séance d'affichage

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

city_map = pygame.image.load("design/city_map.png") #On initialise une variable avec l'image de la ville.
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


print_title = True #On initialise une booléenne. Lorsqu'elle sera fausse, on cessera d'afficher le titre.
print_background = True #Même chose pour le fond d'écran.
print_play_button = True #Même chose pour le bouton play
print_city_map_crop = False #Mêeme chose pour la map de la ville
print_shop = False
print_indoor_shop = False
print_nuclear_central_shop = False
print_nuclear_central_logo = False

police = pygame.font.SysFont(None, 48)
texte = "Bonjour, Pygame!"

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
        if event.type == pygame.MOUSEBUTTONDOWN: #Lorsqu'on appuie sur le bouton entrée, il disparaît
            if play_button_crop_rect.collidepoint(event.pos):
                print_play_button = False
                print_title = False
                print_city_map_crop = True
                print_shop = True
            if (shop_button_crop_rect.collidepoint(event.pos) and print_city_map_crop ==True) or (shop_image_crop_rect.collidepoint(event.pos) and print_city_map_crop==True):
                print_indoor_shop = True
                print_nuclear_central_shop = True
                print_nuclear_central_logo = True
        #Instructions pour pour l'affichage d'une image
        if print_background == True: #tant qu'on met la variable à Vrai, on affiche le fond d'écran
            if background_index >2: #Une suite d'instructions qui font en sorte que les éléments du décor s'affichent avec une certaine latence.
                background_index = 0
            if background_index <=2:
                screen.blit(background_gif[int(background_index)],(0,0))
                background_index = background_index+0.01 #Plus la valeur additionnée sera basse, plus la transition sera lente.

        if print_city_map_crop == True:
            screen.blit(city_map_crop,(0,0))
        if print_shop == True:
            screen.blit(shop_image_crop, (460, 230))
            screen.blit(shop_button_crop, (510,410))
        if print_title == True: #Tant qu'on met la variable à Vrai, on affiche le titre
            screen.blit(title,(-20, image_rect.y))
        if print_play_button == True:
            screen.blit(play_button_crop,(230,300))
        if print_indoor_shop == True:
            screen.blit(wall_indoor_shop_crop,(0,0))
        if print_nuclear_central_shop == True:
            screen.blit(nuclear_central_crop,(0,70))
        if print_nuclear_central_logo == True:
            screen.blit(nuclear_central_button_crop,(65,190))
        pygame.display.update() #Mise à jour continue du programme



pygame.quit()
quit()

