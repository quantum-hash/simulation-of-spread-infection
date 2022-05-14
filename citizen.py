import random

class citoyen:
    les_couleurs = {"I":(245, 55, 10), "NI":(20, 235, 95), "MG":(225, 225, 225)}

    def __init__(self, id, x_pos, y_pos, direction, etat, taille, fenetre, environnement, couleur=None, nom=None, sexe=None, age=None, vaccine=None, masque=None, perimetre=None):
        self.id = id
        self.x = x_pos
        self.y = y_pos
        self.direction = direction
        self.nom = nom
        self.sexe = sexe
        if self.sexe == None:
            self.sexe = random.choice(["H", "F"])  # "H" ou "F"
        self.age = age
        if self.age == None:
            self.age = random.randint(1,100)
        self.etat = etat # "I", "NI", "MG" : Infecte, Non infecte (susceptible), Mort ou gueri
        self.couleur = couleur
        if self.couleur == None:
            if self.etat == "I":
                self.couleur = self.les_couleurs["I"]
            elif self.etat == "NI":
                self.couleur = self.les_couleurs["NI"]
            elif self.etat == "MG":
                self.couleur = self.les_couleurs["MG"]
        self.taille = int(taille)
        self.vaccine = vaccine  # True ou False
        self.masque = masque  # True ou False
        self.fenetre = fenetre
        self.environnement = environnement
        self.contamination = False
        self.perimetre = perimetre
        if self.perimetre == None and self.etat == "I":
            self.perimetre = 15
        if not self.perimetre == None:
            if self.perimetre > 15:
                self.animation_perimetre = [self.perimetre, self.perimetre]
            elif self.perimetre <= 15:
                self.animation_perimetre = [self.perimetre, self.perimetre*2]
        gue = 500
        self.guerison =  random.randint(gue-30,gue+30)
        self.vie = 50
    def bouger (self, vitesse = 1):

        def changer_de_direction(x, y, env, taille, direction):
            if x < env[0]+taille+10 or x > env[2]+env[0]-taille-10 :
                old = direction[0]
                if direction[1] == 0:
                    direction[1] = random.choice([-1, 0, 1])
                if direction[0] == 0:
                    direction[0] = random.choice([-1, 0, 1])
                else:
                    direction[0] = -(direction[0])
                self.x += self.direction[0]*vitesse
                #print( f"-- direction [x] de l'id {self.id} est passe de {old} a {direction[0]} a abscisse :", x)

            if y < env[1]+taille+10 or y > env[3]+env[1]-taille-10 :
                old2 = direction[1]
                if direction[0] == 0:
                    direction[0] = random.choice([-1, 0, 1])
                if direction[1] == 0:
                    direction[1] = random.choice([-1, 0, 1])
                else:
                    direction[1] = -(direction[1])

                self.y += self.direction[1]*vitesse
                #print( f"-- direction [y] de l'id {self.id} est passe de {old2} a {direction[1]} a abscisse :", y)

        # print("-->", self.x, self.y)
        changer_de_direction(self.x, self.y, self.environnement, self.taille, self.direction)
        if self.etat != "MG":
            self.x += self.direction[0]*vitesse
            self.y += self.direction[1]*vitesse


    def verifier_contamination(self, contamine_x, contamine_y, perimetre, vaccin=False, masque=False):
        calcul = (((contamine_x-self.x)**2 + (contamine_y-self.y)**2))**0.5  # racine carre de (carre de (xb-xa) + carre de (yb-ya))
        if calcul <= perimetre*3:
            # Si la personne est trop proche, on devient infecte
            if masque == True or vaccin == True:
                if masque == True and vaccin == True:
                    self.porter_le_masque()
                    if self.contamination == True:
                        self.contamination = False
                        self.se_vacciner()
                    #elif self.contamination == False
                elif masque == True:
                    self.porter_le_masque()
                elif vaccin == True:
                    self.se_vacciner()
            else:
                self.contamination = True
        if self.contamination == True:
            self.etat = "I"
            self.couleur = self.les_couleurs["I"]
            self.perimetre = perimetre
            if self.perimetre > 15:
                self.animation_perimetre = [self.perimetre, self.perimetre]
            elif self.perimetre <= 15:
                self.animation_perimetre = [self.perimetre, self.perimetre*2]

    def verifier_guerison (self):
        if self.etat == 'I':
            self.guerison -= 1
            if self.guerison == 0:
                self.etat = "MG"
                self.couleur = self.les_couleurs["MG"]
                self.perimetre = None

    def se_vacciner (self, pourcentage=42): #  AstraZeneca ==>  34 %,   Pfizer ==>  50 %,   Moyenne des deux vaccins ==>  42 %
        cc = random.randint(1,100)
        if cc > pourcentage:
            self.contamination = True
        # else:
        #     print(cc, self.id)

    def porter_le_masque (self, pourcentage=25): #  ≈25%, source : https://www.quebecscience.qc.ca/sante/efficacite-masque-recentes-etudes/
        cc = random.randint(1,100)
        if cc > pourcentage:
            self.contamination = True
