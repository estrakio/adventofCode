file = open("dataJourUn.txt", "r")
listeData = file.read().split("\n")
totalElf = 0
un = 0
deux = 0
trois = 0
grosGrosElf = 0

for line in listeData:
    if line != "":
        totalElf += int(line)
    else:
        if un < totalElf:
            deux = un
            un = totalElf


        elif deux < totalElf:
            trois = deux
            deux = totalElf

        elif trois < totalElf:
            trois = totalElf

        totalElf = 0




print(un)
print(deux)
print(trois)

grosGrosElf = un + deux + trois

print(grosGrosElf)

