import pygame
import random
import sys

def run_game():
    global resultat
    pygame.init()
    compteur = 30000

    # Définition de la taille de la fenêtre
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
    WINDOW_TITLE = "AIMLABCHARBON"
    BACKGROUND_COLOR = (255, 255, 255)  # Blanc

    # Chargement de l'image de fond
    background = pygame.image.load("design/plant.jpeg")
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
    villepropre = pygame.image.load("design/villepropre.jpg")
    villepropre = pygame.transform.scale(villepropre, (WINDOW_WIDTH, WINDOW_HEIGHT))
    villecharbon = pygame.image.load("design/villecharbon.jpg")
    villecharbon = pygame.transform.scale(villecharbon, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Définition des paramètres des carrés
    SQUARE_SIZE = 50

    # Position du score
    SCORE_POSITION = (WINDOW_WIDTH - 150, 20)
    temps_POSITION = (WINDOW_WIDTH - 150, 80)
    SCORE_FONT = pygame.font.Font(None, 36)

    # Durée de vie des carrés (en millisecondes)
    SQUARE_DURATION = 3750  # 3.75 secondes

    # Temps entre chaque apparition de carré (en millisecondes)
    SQUARE_APPEAR_INTERVAL = 550  # 0.55seconde

    # Chargement de l'image de "coal"
    coal = pygame.image.load("design/coal.png")
    coal = pygame.transform.scale(coal, (SQUARE_SIZE, SQUARE_SIZE))

    # Création de la fenêtre
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()

    # Liste des carrés actuellement affichés à l'écran
    squares = []

    # Score initial
    score = 0

    # Fonction pour générer un carré à une position aléatoire
    def generate_square():
        x = random.randint(0, WINDOW_WIDTH - SQUARE_SIZE)
        y = random.randint(0, WINDOW_HEIGHT - SQUARE_SIZE)
        creation_time = pygame.time.get_ticks()  # Enregistrer le moment de la création
        return (x, y, creation_time)

    # Fonction pour afficher une image pendant un certain temps
    def display_image_for_duration(image, duration):
        window.blit(image, (0, 0))
        pygame.display.flip()
        pygame.time.wait(duration)
        return True

    running = True
    while running:
        # Affichage du titre
        title = pygame.image.load("design/coal.png")
        window.blit(title, (0, 0))
        pygame.display.set_icon(title)

        # Affichage de l'image de fond
        window.blit(background, (0, 0))

        current_time = pygame.time.get_ticks()

        # Génération d'un nouveau carré à chaque intervalle
        if not squares or current_time - squares[-1][2] > SQUARE_APPEAR_INTERVAL:
            new_square = generate_square()
            squares.append(new_square)

        # Affichage et gestion des carrés
        for square in squares[:]:  # Utilisation de la copie de la liste pour itérer
            window.blit(coal, (square[0], square[1]))
            if current_time - square[2] >= SQUARE_DURATION:
                squares.remove(square)  # Retirer le carré si sa durée est écoulée

        # Affichage du score
        score_text = SCORE_FONT.render(f"Score: {score}", True, (0, 0, 0))
        window.blit(score_text, SCORE_POSITION)

        # Affichage du compteur de temps
        temps_text = SCORE_FONT.render(f"Temps: {max(compteur // 1000, 0)}", True, (0, 0, 0))
        window.blit(temps_text, temps_POSITION)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for square in squares[:]:  # Utilisation de la copie de la liste pour itérer
                    square_rect = pygame.Rect(square[0], square[1], SQUARE_SIZE, SQUARE_SIZE)
                    if square_rect.collidepoint(event.pos):
                        squares.remove(square)
                        score += 1

        # appeler la fonction display_image_for_duration
        if score == 30:
            display_image_for_duration(villepropre, 600)
            resultat = True
            print("je renvoie resultat")
            return resultat


        elif compteur <= 0:
            display_image_for_duration(villecharbon, 600)
            resultat = False
            return resultat

        # Décrémentation du compteur de temps
        compteur -= 30  # Décrémenter de 30 millisecondes (équivalent à 30 FPS)

        # Mise à jour de l'affichage
        pygame.display.flip()
        clock.tick(30)



# Exécution de la fonction de jeu
