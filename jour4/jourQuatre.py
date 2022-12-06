file = open("jourQuatre/dataJourQuatre.txt", "r")
listeData = file.read().split("\n")
total = 0

for line in listeData :
    line = line.split(",")
    a  = line[0].split("-") #   3-7 a[0] - a[1]
    b  = line[1].split("-") #   4-6 b[0] - b[1]
    #print(a,"|", b)

    # Conditon 
    #  vérifier si a[0] et plus grand que b[0] et que a[1] est plus petit que b[1] 
    # ou vérifier si b[0] est plus grand que a[0] et b[1] plus petit que a[1] 

    if (int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1])) or (int(b[0]) >= int(a[0]) and int(b[1]) <= int(a[1])) : 
        total += 1

print("la réponse à la partie 1 est ", total)


total2 = 0  
for line in listeData :

    line = line.split(",")
    a  = line[0].split("-") #   3-7 a[0] - a[1] 
    b  = line[1].split("-") #   2-6 b[0] - b[1]
    #print(a,"|", b)

    # Conditon 
    # si a[0] est plus grand que b[0] est plus petit que b[1] ou que b[0] est plus gand que a[0] mais plus petit que a[1]

    if(int(b[1]) >= int(a[0]) >= int(b[0])) or (int(a[1]) >= int(b[0]) >= int(a[0])) : 
        total2 += 1

print("la réponse à la partie 2 est ",total2)