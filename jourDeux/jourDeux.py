# a caillou
# b papier
# c ciseau

# x perdre
# y nul
# z win

caillou =  1
papier = 2
ciseau = 3
win = 6
nul = 3
perdre = 0
listeRound = []
points = 0

file = open("dataJourDeux.txt", "r")
listeData = file.read().split("\n")

def winRate(points, lutin, condition):
    if lutin == "A" and condition == "X" :#
        points += ciseau + perdre# done
    elif lutin == "A" and condition == "Y" :#
        points += caillou + nul# done
    elif lutin == "A" and condition == "Z":#
        points += papier + win# done
    elif lutin == "B" and condition == "X" :#
        points += caillou + perdre# done
    elif lutin == "B" and condition == "Y" :#
        points += papier + nul# done
    elif lutin == "B" and condition == "Z" :#
        points += ciseau + win# done
    elif lutin == "C" and condition == "X" :#
        points += papier + perdre # done
    elif lutin == "C" and condition == "Y" :#
        points += ciseau + nul# done
    elif lutin == "C" and condition == "Z" :#
        points += caillou + win#


    return points


for round in listeData :
    listeRound.append(round.split(" "))

for round in listeRound:
    points = winRate(points, round[0], round[1])


print(points)