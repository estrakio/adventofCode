


total = 0
x = 1
file = open("dataJourTrois.txt", "r")
listeData = file.read().split("\n")


for a in listeData :
    b = len(a)
    moitie = b / 2
    for i in range(int(moitie)):

        while x <= int(moitie) :
            if a[i] == a[-x]:
                if a[i].isupper() :
                    data = a[i].lower()
                    calc = ord(data) - 96
                    total += calc + 26
                else :
                    calc = ord(a[i]) - 96
                    total += calc
            x += 1
        x = 1

