file = open("jour7/data7.txt", "r")
listeData = file.read().split("\n")
list = {}

path=  ""

print("\n" *25)
for line in listeData :
    # Découpage de la ligne en plusieurs donnée sélectable :
    line = line.split(" ")

    if line[1] == "cd" and line[2] == "/":
        path = line[2]
        list[path] = 0

    # Vérification si la ligne et un déplacement dans un directory
    elif line[1] == "cd" and line[2] != "..":
        
        path = path  + ";" + line[2]
        list[path] = 0


    # Vérification si la ligne et une sortie de directory :
    if line[1] == "cd" and line[2] == "..":
        
        a = path.split(";")
        a.pop()
        path = ""
        for line in a : 
            if line == "/" :
                path += line
            else: 
                path += ";"+ line
        

    # Vérification si la donnée est bien un int 
    if line[0].isnumeric() :
        #print(path)
        listPath = path.split(';')
        data = ""
        for file in  listPath: 
            data +=  file  
            list[data] += int(line[0])
            data += ';'


total =  0 
for champ in list : 
    
    total += list[champ]

print("reponse partie 1",total)
print("l'espace libra actuel est de :", 70000000 - int(list["/"]))
print("Espace disque occupé actuel = ",int(list["/"]))
print("L'espace de stockage à libéré est de :", int(list["/"]) - 40000000)
res = 70000000
for champ in list : 
    if list[champ] >= int(list["/"]) - 40000000 : 
        if list[champ] <= res :
            res = list[champ]
            nom = champ
            
print("le dossier", nom,"est le plus petit fichier a supprimer il contient :",res,"données")


print("\n"*2)