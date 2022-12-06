


total = 0
x = 1
file = open("jourTrois/dataJourTrois.txt", "r")
listeData = file.read().split("\n")
moitieUn = []
moitieDeux = []

for a in listeData :
    b = len(a) // 2

    moitieUn = a[0 : b]
    moitieDeux = a[b : len(a)]
    for i in range(len(moitieUn)) :
        if moitieDeux.__contains__(moitieUn[i]) : 
            if moitieUn[i].isupper() :
                    total += ord(moitieUn[i]) - 38
            else :
                    total += ord(moitieUn[i]) - 96

            break


print(" le résultat de la partie 1 et : ", total)

elfUn = ""
elfDeux = ""
elfTrois = ""
totalDeux = 0
for a in range(0, len(listeData), 3) :


    elfUn = listeData[a]
    elfDeux = listeData[a+1]
    elfTrois = listeData[a+2]

    for i in range(len(elfUn)) :
                if elfDeux.__contains__(elfUn[i]) and elfTrois.__contains__(elfUn[i]): 
                    if elfUn[i].isupper() :
                        totalDeux += ord(elfUn[i]) - 38
                    else :
                        totalDeux += ord(elfUn[i]) - 96
                    break
                    
print(" le résultat de la partie 2 et : ", totalDeux)
