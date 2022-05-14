import pygame, pylab, matplotlib, time, random, math
# from pygame.locals import *
import matplotlib.backends.backend_agg as agg
matplotlib.use("Agg")


from population import population
from window import fenetre
from citizen import citoyen

if __name__ == "__main__":
    # fenetre
    fenetre = fenetre(1200, 500, "Simulation epidemie GEII")
    pygame.init()
    couleur = (255, 0, 0)
    taille_env = 800, 440
    color_light = (170,170,170)
    color_dark = (100,100,100)
    mouse = pygame.mouse.get_pos()
    size_button = 9

    # creation de l'environnement
    fenetre.creer_environnement(taille_env, couleur)

    # citoyen
    taille = 10
    citoyens = []
    les_contamines = []
    perimetre_infecte = 15

    # population
    nombre_infectes = 10
    nombre_susceptibles = 10
    i, ni, mg = [nombre_infectes], [nombre_susceptibles], [0]
    les_couleurs = {"I":(245, 55, 10), "NI":(20, 235, 95), "MG":(225, 225, 225)}

    population = population(nombre_infectes, nombre_susceptibles)
    population.creer_population(fenetre.environnement, taille)
    taille_population = len(population.infectes)+len(population.susceptibles)

    for infecte in population.infectes:
        OBJET = citoyen(infecte, population.infectes[infecte][0], population.infectes[infecte][1], population.infectes[infecte][2], "I", taille, fenetre, fenetre.environnement, perimetre=perimetre_infecte)
        citoyens.append(OBJET)
        les_contamines.append(OBJET)
    for susceptible in population.susceptibles:
        citoyens.append(citoyen(susceptible, population.susceptibles[susceptible][0], population.susceptibles[susceptible][1], population.susceptibles[susceptible][2], "NI", taille, fenetre, fenetre.environnement))

    fonctionnement = True
    while fonctionnement:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fonctionnement = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fonctionnement = False
                    break
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    fig = pylab.figure(figsize=[3, 3], # Inches
                                       dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                                       )
                    ax = fig.gca()
                    ax.plot(i)
                    ax.plot(ni)
                    ax.plot(mg)
                    # ax.plot(ni)
                    canvas = agg.FigureCanvasAgg(fig)
                    canvas.draw()
                    renderer = canvas.get_renderer()
                    raw_data = renderer.tostring_rgb()

                    screen = pygame.display.get_surface()
                    size = canvas.get_width_height()
                    surf = pygame.image.fromstring(raw_data, size, "RGB")
                    screen.blit(surf, (fenetre.environnement[0]+fenetre.environnement[2]+10, fenetre.environnement[1]+taille_texte*difference_taille*3))
                    pygame.display.flip()
                    time.sleep(10)
            elif event.type == pygame.MOUSEBUTTONDOWN:

                #if the mouse is clicked on the buttons
                if b_i_moins[0]-size_button/2 <= mouse[0] <= b_i_moins[0]+size_button*1.5 and  b_i_moins[1] <= mouse[1] <=  b_i_moins[1]+size_button*2:
                    try:
                        bye = random.choice(les_contamines)
                        les_contamines.remove(bye)
                        citoyens.remove(bye)
                    except IndexError:
                        pass

                elif b_i_plus[0]-size_button/2 <= mouse[0] <= b_i_plus[0]+size_button*1.5 and  b_i_plus[1] <= mouse[1] <= b_i_plus[1]+size_button*2:
                    taille_population+= 1
                    tpi = taille_population
                    x_tpi = random.randint(fenetre.environnement[0]+taille, fenetre.environnement[2]+fenetre.environnement[0]-taille)
                    y_tpi = random.randint(fenetre.environnement[1]+taille, fenetre.environnement[3]+fenetre.environnement[1]-taille)
                    direct_tpi = random.choice(list({"1": [0, 1], "2": [round(math.sqrt(2), 1)/2, round(math.sqrt(2), 1)/2], "3": [1, 0], "4": [round(math.sqrt(2), 1)/2, -(round(math.sqrt(2), 1)/2)], "5": [0, -1], "6": [-(round(math.sqrt(2), 1)/2), -(round(math.sqrt(2), 1)/2)], "7": [-1, 0], "8": [-(round(math.sqrt(2), 1)/2), round(math.sqrt(2), 1)/2]}.values()))
                    OBJET = citoyen(tpi, x_tpi, y_tpi, direct_tpi, "I", taille, fenetre, fenetre.environnement, perimetre=perimetre_infecte)
                    citoyens.append(OBJET)
                    les_contamines.append(OBJET)
                elif b_ni_moins[0]-size_button/2 <= mouse[0] <= b_ni_moins[0]+size_button*1.5 and  b_ni_moins[1] <= mouse[1] <=  b_ni_moins[1]+size_button*2:
                    try:
                        bye = random.choice([it for it in citoyens if it not in les_contamines])
                        citoyens.remove(bye)
                    except IndexError:
                        pass
                elif b_ni_plus[0]-size_button/2 <= mouse[0] <= b_ni_plus[0]+size_button*1.5 and  b_ni_plus[1] <= mouse[1] <= b_ni_plus[1]+size_button*2:
                    taille_population+= 1
                    tpi = taille_population
                    x_tpi = random.randint(fenetre.environnement[0]+taille, fenetre.environnement[2]+fenetre.environnement[0]-taille)
                    y_tpi = random.randint(fenetre.environnement[1]+taille, fenetre.environnement[3]+fenetre.environnement[1]-taille)
                    direct_tpi = random.choice(list({"1": [0, 1], "2": [round(math.sqrt(2), 1)/2, round(math.sqrt(2), 1)/2], "3": [1, 0], "4": [round(math.sqrt(2), 1)/2, -(round(math.sqrt(2), 1)/2)], "5": [0, -1], "6": [-(round(math.sqrt(2), 1)/2), -(round(math.sqrt(2), 1)/2)], "7": [-1, 0], "8": [-(round(math.sqrt(2), 1)/2), round(math.sqrt(2), 1)/2]}.values()))
                    OBJET = citoyen(tpi, x_tpi, y_tpi, direct_tpi, "NI", taille, fenetre, fenetre.environnement)
                    citoyens.append(OBJET)
        fenetre.creer_environnement(taille_env, couleur)
        total = {"infectes": 0, "susceptibles": 0, "morts ou gueris": 0}

        mgg = []
        for individu in citoyens:
            if individu.etat == "I":
                total["infectes"] += 1
                # les_contamines.append([individu.x, individu.y])
                individu.verifier_guerison()
                if individu.etat == "MG":
                    # print(les_contamines)
                    # print(individu)
                    les_contamines.remove(individu)
            elif individu.etat == "NI":
                total["susceptibles"] += 1
                for contamine in les_contamines:
                    individu.verifier_contamination(contamine.x, contamine.y, contamine.perimetre, vaccin=True, masque=True)
                if individu.etat == "I":
                    les_contamines.append(individu)
            elif individu.etat == "MG":
                total["morts ou gueris"] += 1
                mgg.append(individu)
                if total["morts ou gueris"] > 20:
                    citoyens.remove(random.choice(mgg))
            # print(individu.__dict__)
            # print(dir(individu))
            individu.bouger(vitesse = 1)
            pygame.draw.circle(individu.fenetre.fenetre, individu.couleur, (individu.x, individu.y), individu.taille)

            #print(individu.perimetre)
            if individu.perimetre != None: #perimetre pour les infectes
                #print(individu.animation_perimetre)
                if not individu.animation_perimetre[0] == 0:
                    pygame.draw.circle(individu.fenetre.fenetre, individu.couleur, (individu.x, individu.y), individu.taille+individu.animation_perimetre[0], 1)
                    individu.animation_perimetre[0] -= 1
                else:
                    individu.animation_perimetre[1] -= 1
                    if individu.animation_perimetre[1] == 0:
                        if individu.perimetre > 15:
                            individu.animation_perimetre = [individu.perimetre, individu.perimetre]
                        elif individu.perimetre <= 15:
                            individu.animation_perimetre = [individu.perimetre, individu.perimetre*2]

            taille_texte = 6
            myfont0 = pygame.font.SysFont('Arial', taille_texte*2)
            textsurface = myfont0.render(str(individu.id), False, (255, 255, 255))
            fenetre.fenetre.blit(textsurface, (individu.x, individu.y))

        difference_taille = 3
        myfont = pygame.font.SysFont('Arial', taille_texte*difference_taille)
        I_TEXTE = myfont.render("Susceptibles => "+str(total["susceptibles"]), 1, les_couleurs["NI"])
        fenetre.fenetre.blit(I_TEXTE, (fenetre.environnement[0]+fenetre.environnement[2]+10, fenetre.environnement[1]))
        NI_TEXTE = myfont.render("Infectes => "+str(total["infectes"]), 1, les_couleurs["I"])
        fenetre.fenetre.blit(NI_TEXTE, (fenetre.environnement[0]+fenetre.environnement[2]+10, fenetre.environnement[1]+5+taille_texte*difference_taille))
        MG_TEXTE = myfont.render("Morts ou gueris => "+str(total["morts ou gueris"]), 1, les_couleurs["MG"])
        fenetre.fenetre.blit(MG_TEXTE, (fenetre.environnement[0]+fenetre.environnement[2]+10, fenetre.environnement[1]+10+taille_texte*difference_taille*2))

# boutons d'ajout d'infectes ou susceptibles
        mouse = pygame.mouse.get_pos()

        where = max([NI_TEXTE.get_width(), I_TEXTE.get_width(), MG_TEXTE.get_width()])+100
        b_ni_moins = (fenetre.environnement[0]+fenetre.environnement[2]+where, fenetre.environnement[1])
        b_ni_plus = (fenetre.environnement[0]+fenetre.environnement[2]+25+where, fenetre.environnement[1])

        b_i_moins = (fenetre.environnement[0]+fenetre.environnement[2]+where, fenetre.environnement[1]+5+taille_texte*difference_taille)
        b_i_plus = (fenetre.environnement[0]+fenetre.environnement[2]+25+where, fenetre.environnement[1]+5+taille_texte*difference_taille)

#b_i_moins
        if b_i_moins[0]-size_button/2 <= mouse[0] <= b_i_moins[0]+size_button*1.5 and  b_i_moins[1] <= mouse[1] <=  b_i_moins[1]+size_button*2:
            pygame.draw.circle(fenetre.fenetre, color_light, [b_i_moins[0]-4+size_button,b_i_moins[1]+size_button/4+size_button], size_button, 0)

        else:
            pygame.draw.circle(fenetre.fenetre, color_dark, [b_i_moins[0]-4+size_button,b_i_moins[1]+size_button/4+size_button], size_button, 0)
        fenetre.fenetre.blit(pygame.font.SysFont('Arial', taille_texte*difference_taille).render('-' , True , les_couleurs["I"]) , (b_i_moins[0]+2,b_i_moins[1]-2))
#b_i_plus
        if b_i_plus[0]-size_button/2 <= mouse[0] <= b_i_plus[0]+size_button*1.5 and  b_i_plus[1] <= mouse[1] <= b_i_plus[1]+size_button*2:
            pygame.draw.circle(fenetre.fenetre, color_light, [b_i_plus[0]-4+size_button,b_i_plus[1]+size_button/4+size_button], size_button, 0)

        else:
            pygame.draw.circle(fenetre.fenetre, color_dark, [b_i_plus[0]-4+size_button,b_i_plus[1]+size_button/4+size_button], size_button, 0)
        fenetre.fenetre.blit(pygame.font.SysFont('Arial', taille_texte*difference_taille).render('+' , True , les_couleurs["I"]) , (b_i_plus[0],b_i_plus[1]))

#b_ni_moins
        if b_ni_moins[0]-size_button/2 <= mouse[0] <= b_ni_moins[0]+size_button*1.5 and  b_ni_moins[1] <= mouse[1] <=  b_ni_moins[1]+size_button*2:
            pygame.draw.circle(fenetre.fenetre, color_light, [b_ni_moins[0]-4+size_button,b_ni_moins[1]+size_button/4+size_button], size_button, 0)

        else:
            pygame.draw.circle(fenetre.fenetre, color_dark, [b_ni_moins[0]-4+size_button,b_ni_moins[1]+size_button/4+size_button], size_button, 0)
        fenetre.fenetre.blit(pygame.font.SysFont('Arial', taille_texte*difference_taille).render('-' , True , les_couleurs["NI"]) , (b_ni_moins[0]+2,b_ni_moins[1]-2))
#b_ni_plus
        if b_ni_plus[0]-size_button/2 <= mouse[0] <= b_ni_plus[0]+size_button*1.5 and  b_ni_plus[1] <= mouse[1] <= b_ni_plus[1]+size_button*2:
            pygame.draw.circle(fenetre.fenetre, color_light, [b_ni_plus[0]-4+size_button,b_ni_plus[1]+size_button/4+size_button], size_button, 0)

        else:
            pygame.draw.circle(fenetre.fenetre, color_dark, [b_ni_plus[0]-4+size_button,b_ni_plus[1]+size_button/4+size_button], size_button, 0)
        fenetre.fenetre.blit(pygame.font.SysFont('Arial', taille_texte*difference_taille).render('+' , True , les_couleurs["NI"]) , (b_ni_plus[0],b_ni_plus[1]))

        if total["infectes"] != i[-1]:
            print(total["infectes"], end=" -> ")
            i.append(total["infectes"])
        if total["susceptibles"] != ni[-1]:
            ni.append(total["susceptibles"])
        if total["morts ou gueris"] != mg[-1]:
            mg.append(total["morts ou gueris"])



        pygame.display.update()
        fenetre.fenetre.fill((0, 0, 0))
        vitesse_cpu = 100
        pygame.time.Clock().tick(vitesse_cpu)
