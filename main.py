import pygame
import os
wallet = 1000000
bag = []
shop = {"parc_dattraction" : 1000000, "aire_de_jeu" : 10000, "statue" : 1500, "magasin_de_fleurs": 200000, "caserne_douvriers": 3000, "petite_centrale" : 8000}
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

open_the_shop(shop)
see_the_wallet(wallet)
buy_in_the_shop(shop, bag, wallet)
print_bag(bag)

title_logo = "design/pixilart-drawing.png" #Variable avec le logo "CenTown"
screen_title_background = "design/frame-1.gif" #Variable avec le le fond d'écran de l'usine
open
pygame.init() #Initialisation de la séance d'affichage

screen = pygame.display.set_mode((640, 455)) #L'écran affiché est de la taille 640 x 455
pygame.display.set_caption("CenTown") #Le titre de la fenêtre est "CenTown"

title = pygame.image.load(title_logo) #L'image jpg du logo est mis dans un format spécial dans la variable pygame. C'est le format "surface", nécessaire pour que pygame l'utilise.
background = pygame.image.load(screen_title_background).convert() #Même chose pour la fond d'écran
nouvelle_taille = (640,455) #On initialise une nouvelle taille
image_redimensionnee = pygame.transform.scale(background,nouvelle_taille) #On redimensionne le fond d'écran en fonction de cette nouvelle taille

image_rect = title.get_rect() #On met les coordonnées du logo dans une variable qu'on modifiera

print_title = True #On initialise une booléenne. Lorsqu'elle sera fausse, on cessera d'afficher le titre.
print_background = True #Même chose pour le fond d'écran.

run = False
while run: #Tant que le programme est en cours
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Tant que la croix n'a pas été cliqué, le programme continue
                run = False
        if event.type == pygame.KEYDOWN: #Si la flèche du bas est saisie
            if event.key == pygame.K_DOWN and image_rect.y < 170:
                image_rect.y += 2 #L'ordonnée de l'image est modifiée, elle ne peut pas sortir de l'image grâce à la condition du dessus.
            if event.key == pygame.K_UP and image_rect.y > -90: #Si la flèche du haut est saisia
                image_rect.y -= 2 #Même chose que plus haut
        elif event.type == pygame.KEYDOWN: #Si la touche entrée est saisie, on arrête l'affichage du titre
            if event.key == pygame.K_RETURN:
                print_title = False

        if print_background == True: #tant qu'on met la variable à Vrai, on affiche le fond d'écran
            screen.blit(image_redimensionnee,(0,0))
        if print_title == True: #Tant qu'on met la variable à Vrai, on affiche le titre
            screen.blit(title,(-20, image_rect.y))

        pygame.display.update() #Mise à jour continue du programme

pygame.quit()
quit()
