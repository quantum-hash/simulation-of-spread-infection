import math, random

class population:
    def __init__(self, nombre_infectes: int, nombre_susceptibles: int) -> None:
        self.nombre_infectes = nombre_infectes
        self.nombre_susceptibles = nombre_susceptibles
        self.infectes = {}
        self.susceptibles = {}
        self.direction = {"1": [0, 1], "2": [round(math.sqrt(2), 1)/2, round(math.sqrt(2), 1)/2], "3": [1, 0], "4": [round(math.sqrt(2), 1)/2, -(round(math.sqrt(2), 1)/2)], "5": [0, -1], "6": [-(round(math.sqrt(2), 1)/2), -(round(math.sqrt(2), 1)/2)], "7": [-1, 0], "8": [-(round(math.sqrt(2), 1)/2), round(math.sqrt(2), 1)/2]}

    def creer_population(self, environnement: 'pygame.Rect object', taille: int, direction: "1->8" = None) -> None:
        count1 = 0
        for _ in range(self.nombre_infectes):
            x = random.randint(environnement[0]+taille, environnement[2]+environnement[0]-taille)
            y = random.randint(environnement[1]+taille, environnement[3]+environnement[1]-taille)
            if direction == None:
                direct = random.choice(list(self.direction.keys()))
            else:
                direct = direction
            self.infectes[str(count1)] = x , y, self.direction[direct]  # exemple: (225, 360, (0, 1))
            count1+=1
        for _ in range(self.nombre_susceptibles):
            x = random.randint(environnement[0]+taille, environnement[2]+environnement[0]-taille)
            y = random.randint(environnement[1]+taille, environnement[3]+environnement[1]-taille)
            if direction == None:
                direct = random.choice(list(self.direction.keys()))
            else:
                direct = direction
            self.susceptibles[str(count1)] = x , y, self.direction[direct]
            count1+=1
        print(self.infectes, self.susceptibles)
