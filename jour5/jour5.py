file = open("jour5/data5.txt", "r")
listeData = file.read().split("\n")

t1 = ["J", "H", "P", "M", "S", "F", "N", "V"]
t2 = ["S", "R", "L", "M", "J", "D", "Q"] 
t3 = ["N", "Q", "D", "H", "C", "S", "W", "B"]
t4 = ["R", "S", "C", "L"]
t5 = ["M", "V", "T", "P", "F", "B"]
t6 = ["T", "R", "Q", "N", "C"]
t7 = ["G", "V", "R"]  
t8 = ["C", "Z", "S", "P", "D", "L", "R"]
t9 = ["D", "S", "J", "V", "G", "P", "B", "F"]


for i in listeData: 
    command = i.split(" ")
    # command[1] = combien de caisse à bouger 
    # command[3] = depuis
    #  command[5] = vers
    for i in range(int(command[1])):
        locals()["t"+command[5]].append(locals()["t"+str(command[3])][-1])
        del locals()["t"+command[3]][-1]


motMagique = t1[-1] + t2[-1] + t3[-1] + t4[-1] + t5[-1] + t6[-1] + t7[-1] + t8[-1] + t9[-1]

print("Résultat exo 1", motMagique)

t1 = ["J", "H", "P", "M", "S", "F", "N", "V"]
t2 = ["S", "R", "L", "M", "J", "D", "Q"] 
t3 = ["N", "Q", "D", "H", "C", "S", "W", "B"]
t4 = ["R", "S", "C", "L"]
t5 = ["M", "V", "T", "P", "F", "B"]
t6 = ["T", "R", "Q", "N", "C"]
t7 = ["G", "V", "R"]  
t8 = ["C", "Z", "S", "P", "D", "L", "R"]
t9 = ["D", "S", "J", "V", "G", "P", "B", "F"]

for i in listeData: 
    command = i.split(" ")
    # command[1] = combien de caisse à bouger 
    # command[3] = depuis
    #  command[5] = vers
    for i in range(int(command[1])):
        locals()["t"+command[5]].append(locals()["t"+str(command[3])][-int(command[1]) + i])
        del locals()["t"+command[3]][-int(command[1]) + i]

motMagique2 = t1[-1] + t2[-1] + t3[-1] + t4[-1] + t5[-1] + t6[-1] + t7[-1] + t8[-1] + t9[-1]

print("Résultat exo 2", motMagique2)
