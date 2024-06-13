import pygame
import sys
import random

def jeux2():
  global resultat2
  pygame.init()
  
  # Couleurs
  ROUGE = (255, 0, 0)
  NOIR = (0, 0, 0)
  
  # Paramètres de la fenêtre
  largeur_fenetre = 600
  hauteur_fenetre = 400
  fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
  pygame.display.set_caption("Évite les carrés !")
  
  # Chargement de l'image d'arrière-plan
  arriere_plan = pygame.image.load("route.png").convert()
  arriere_plan = pygame.transform.scale(arriere_plan, (largeur_fenetre, hauteur_fenetre))
  
  # Paramètres du joueur
  joueur_taille = 40  # Taille augmentée pour correspondre à l'image "voiture.png"
  joueur_pos_x = (largeur_fenetre - joueur_taille) // 2  # Fixe, le joueur ne se déplace pas horizontalement
  joueur_pos_y = (hauteur_fenetre - joueur_taille) // 2
  joueur_deplacement = 10  # Incrément de déplacement vertical
  
  # Chargement de l'image du joueur
  image_voiture = pygame.image.load("voiture.png").convert_alpha()
  image_voiture = pygame.transform.scale(image_voiture, (joueur_taille, joueur_taille))
  
  # Paramètres des obstacles
  carre_taille_initial = 40
  carre_taille = carre_taille_initial  # Taille initiale des obstacles (40 pixels)
  carre_vitesse = 400  # Vitesse en pixels par seconde
  carre_liste = []
  
  # Chargement et redimensionnement des images des obstacles
  images = [
      pygame.image.load("coal.png").convert_alpha(),
      pygame.image.load("poubelle.png").convert_alpha(),
      pygame.image.load("chat.png").convert_alpha(),
      pygame.image.load("egout.png").convert_alpha()
  ]
  
  # Redimensionnement des images des obstacles
  for i in range(len(images)):
      images[i] = pygame.transform.scale(images[i], (carre_taille, carre_taille))
  
  # Fonction pour générer un nouvel obstacle avec une image aléatoire
  def nouveau_carre():
      x = largeur_fenetre
      y = random.randrange(0, hauteur_fenetre - carre_taille)
      image = random.choice(images)
      carre_liste.append([x, y, image])
  
  # Fonction pour dessiner le joueur (maintenant une image de voiture)
  def dessiner_joueur(x, y):
      fenetre.blit(image_voiture, (x, y))
  
  # Fonction pour dessiner un obstacle (maintenant une image)
  def dessiner_carre(x, y, image):
      fenetre.blit(image, (x, y))
  
  # Fonction pour détecter les collisions
  def collision(joueur_x, joueur_y, joueur_taille, carre_x, carre_y, carre_taille):
      joueur_rect = pygame.Rect(joueur_x, joueur_y, joueur_taille, joueur_taille)
      carre_rect = pygame.Rect(carre_x, carre_y, carre_taille, carre_taille)
      return joueur_rect.colliderect(carre_rect)
  
  # Initialiser le temps de départ pour le compte à rebours de 15 secondes
  compte_a_rebours = 16
  temps_debut = pygame.time.get_ticks()
  
  # Boucle principale du jeu
  clock = pygame.time.Clock()  # Pour contrôler la vitesse de mise à jour
  start_time = pygame.time.get_ticks()  # Enregistrer l'heure de début
  
  while True:
      # Gestion des événements
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
  
      # Obtenir le temps écoulé depuis le début du jeu
      elapsed_time = pygame.time.get_ticks() - start_time
  
      # Nettoyer l'écran et dessiner l'image d'arrière-plan
      fenetre.blit(arriere_plan, (0, 0))
  
      # Dessiner le joueur (la position x reste constante)
      dessiner_joueur(joueur_pos_x, joueur_pos_y)
  
      if elapsed_time > 1000:  # Attendre 1 seconde avant de commencer le jeu
          # Déplacement vertical du joueur (par incréments de 10 pixels)
          keys = pygame.key.get_pressed()
          if keys[pygame.K_UP] and joueur_pos_y > 0:
              joueur_pos_y -= joueur_deplacement
          if keys[pygame.K_DOWN] and joueur_pos_y < hauteur_fenetre - joueur_taille:
              joueur_pos_y += joueur_deplacement
  
          # Générer de nouveaux obstacles (images)
          if len(carre_liste) < 3:  # Limiter le nombre d'obstacles à l'écran à 3
              nouveau_carre()
  
          # Déplacer et dessiner les obstacles
          for carre in carre_liste:
              carre[0] -= carre_vitesse / 60  # Déplacement ajusté pour correspondre à 400 pixels par seconde à 60 FPS
              dessiner_carre(carre[0], carre[1], carre[2])
  
              # Si l'obstacle sort de l'écran, le supprimer
              if carre[0] < -carre_taille:
                  carre_liste.remove(carre)
  
              # Vérifier la collision
              if collision(joueur_pos_x, joueur_pos_y, joueur_taille, carre[0], carre[1], carre_taille):
                  # Afficher un message de défaite
                  font = pygame.font.SysFont(None, 75)
                  texte = font.render('Défaite!', True, ROUGE)
                  fenetre.blit(texte, [(largeur_fenetre - texte.get_width()) // 2, (hauteur_fenetre - texte.get_height()) // 2])
                  pygame.display.update()
                  pygame.time.wait(1000)  # Attendre 1 seconde avant de quitter
                  resultat2=FALSE
  
          # Calculer le temps restant pour le compte à rebours de 15 secondes
          temps_restant = compte_a_rebours - (pygame.time.get_ticks() - temps_debut) // 1000
  
          # Afficher le compteur de temps restant
          font = pygame.font.SysFont(None, 50)
          texte = font.render(f"Temps: {temps_restant}", True, NOIR)
          text_rect = texte.get_rect()
          text_rect.right = largeur_fenetre - 10
          text_rect.top = 10
          fenetre.blit(texte, text_rect)
  
          # Vérifier si le temps est écoulé
          if temps_restant <= 0:
              # Afficher un message de victoire
              font = pygame.font.SysFont(None, 75)
              texte = font.render('Victoire!', True, ROUGE)
              fenetre.blit(texte, [(largeur_fenetre - texte.get_width()) // 2, (hauteur_fenetre - texte.get_height()) // 2])
              pygame.display.update()
              pygame.time.wait(2000)
              resultat2=TRUE
  
      # Mettre à jour l'affichage
      pygame.display.update()
  
      # Contrôler la vitesse du jeu pour 60 FPS
      clock.tick(60)
