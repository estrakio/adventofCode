file = open("jour8/data8.txt", "r")
listeData = file.read().split("\n")
total = 0



# fonction de création du tableau
def creationTableau(listeData) :
    w, h = len(listeData), len(listeData[0])
    tableau = [[0 for x in range(h)] for y in range(w)] 
    return tableau

# fonction d'attribution des valeurs dans le tableau
def attributionDataTableau(listeData, tableau): 
    for x in range(len(listeData)):
        for y in range(len(listeData[0])) :
            tableau[x][y] = listeData[x][y]

# fonction qui permet de vérifier si la cellule fait parti d'un des coté du tableau :
# NUL SERT A RIEN 
def faitPartiDesBords(posX, posY, tailleLigne, tailleColonne):
    # print("posX", posX, "posY", posY, "tailleLigne", tailleLigne, "tailleColonne", tailleColonne)
    if posX == 0 or posX == tailleColonne-1 :
        #print("ok")
        return 1
    elif posY == 0 or posY == tailleLigne-1 :
        #print("ok")
        return 1
    else :
        return 0

# Fonction qui vérifie si l'arbre et visible depuis l'exterieur
def estCacher(posX, posY, tailleLigne, tailleColonne, tailleArbre) :
    a = 0
    if posX != 0 or posY != 0 or posX == tailleColonne-1 or posY == tailleLigne-1 :

        # Vérification si les arbres à gauche sont plus grand
        i = posY - 1
        while i >= 0 : 
            if tailleArbre <= tableau[posX][i] :
                a += 1
                break
            i -= 1

        # Vérification si les arbres à droite sont plus grand 
        i = posY + 1
        while i < tailleLigne : 
            if tailleArbre <= tableau[posX][i] :
                a += 1
                break
            i += 1

        # Vérification si les arbres du dessus sont plus grand 
        i = posX - 1
        while i >= 0 : 
            if tailleArbre <= tableau[i][posY] :
                a += 1
                break
            i -= 1
        # Vérification si les arbres du dessous sont plus grand
        i = posX + 1
        while i < tailleLigne : 
            if tailleArbre <= tableau[i][posY] :
                a += 1
                break
            i += 1


    if a == 4 :
        return 1
    
    return 0

# Fonction qui vérifie si l'arbre et visible depuis l'exterieur
def renaultScenic(forest, x, y):
    a = 1





tableau = creationTableau(listeData = listeData)
attributionDataTableau(listeData= listeData, tableau= tableau)
for x in range(len(tableau)):
    for y in range(len(tableau[0])) :
        
        #if faitPartiDesBords(posX = x, posY= y, tailleLigne = len(tableau[0]), tailleColonne= len(tableau)) :
        #    total += 1
        if not estCacher(posX = x, posY = y, tailleLigne = len(tableau[0]), tailleColonne= len(tableau), tailleArbre = tableau[x][y]) :
            total += 1
        


print("total d'arbres dans les coté =", total)
# print("Nombre de colonne =", len(tableau[0]))
# print("nombre de ligne =", len(tableau))
# print(tableau)


