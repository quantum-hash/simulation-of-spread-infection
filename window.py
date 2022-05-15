import pygame

class fenetre:
    def __init__(self, longueur: int, largeur: int, nom_fenetre: str = "Simulation epidemie GEII", nom_icone: str = 'icone.jpg') -> None:
        self.fenetre = pygame.display.set_mode(
            (longueur, largeur))  # Creation de la fenetre
        pygame.display.set_caption(nom_fenetre)
        try:
            pygame.image.load(nom_icone)
            pygame.display.set_icon(icone)
        except FileNotFoundError:
            pass

    def creer_environnement(self, taille_env: tuple, couleur: tuple, forme: "carre" or "cercle" = "carre") -> None:
        """
        couleur: tuple(red: int, green: int, blue: int)
        """
        if forme == "carre":
            self.environnement = pygame.draw.rect(
                self.fenetre, couleur, pygame.Rect(30, 30, taille_env[0], taille_env[1]),  1)
        elif forme == "cercle":
            self.environnement = pygame.draw.circle(self.fenetre, couleur,
                   [200,200], (taille_env[0]+taille_env[1])/7, 1)
