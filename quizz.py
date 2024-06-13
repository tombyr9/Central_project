import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH = 640
HEIGHT = 455
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 30

# Définition des questions et réponses
questions = [
    "Quel est le gaz responsable du réchauffement climatique ?",
    "Qui sont les scientifique qui étudient le climat ?",
    "Quelle est la principale cause de pollution ?",
    "Quel est l'effet du charbon sur l'air ?",
    "Quel impact a l'exploitation minière du charbon ?",
    "Pourquoi le charbon est dit non renouvelable ? Car",
    "Quel effet a le charbon ?",
    "Pourquoi l'énergie nucléaire est dites d'énergie propre ? Car"
]

answers = [
    ["Gaz a effet de serre", "Gaz de serre", "Gaz toxique", "Gaz naturel"],
    ["Le giec", "L’onu", "Brics", "Pas de nom"],
    ["Nucléaire", "Hydraulique", "Charbon", "Pétrole"],
    ["améliore la qualité de l'air",
     "contribue à la pollution de l'air",
     "aucun impact",
     "produit de l'oxygène en brûlant"],
    ["favorise la biodiversité",
     "détruit les écosystèmes",
     "aucun impact",
     "protège les zones sauvages"],
    ["fabriqué à partir de matières recyclées",
     "produit en grandes quantités",
     "se forme naturellement et rapidement",
     "se forme durant des millions d'années"],
    ["contribue à refroidir la planète",
     "réduit les émissions de CO2",
     "accélère le réchauffement de la planète",
     "aucun impact"],
    ["produit moins de déchets que les autres",
     "elle n'émet aucun gaz"]
]

correct_choices = [0, 0, 2, 1, 1, 3, 2, 0]  # Index des bonnes réponses pour chaque question

# Initialisation de la fenêtre principale
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz sur l'environnement")

# Chargement de l'image de fond
background = pygame.image.load("design/pixel.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Initialisation de la police
font = pygame.font.SysFont(None, FONT_SIZE)


# Fonction pour afficher le texte
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


# Fonction pour afficher les questions et les réponses
def show_question(question_index):
    screen.blit(background, (0, 0))
    draw_text(questions[question_index], font, BLACK, screen, WIDTH // 2, HEIGHT // 4)

    # Affichage des réponses sous forme de boutons
    buttons = []
    for i, answer in enumerate(answers[question_index]):
        button_rect = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 + i * 50, 400, 40)
        pygame.draw.rect(screen, BLACK, button_rect, 2)
        draw_text(answer, font, BLACK, screen, button_rect.centerx, button_rect.centery)
        buttons.append(button_rect)

    return buttons


# Fonction pour afficher l'écran de démarrage
def show_start_screen():
    screen.blit(background, (0, 0))
    draw_text("Appuyez sur Start pour commencer", font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
