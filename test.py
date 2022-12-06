listeData = "move 3 from 8 to 4"
t4 = ["R", "S", "C", "L"]
t8 = ["C", "Z", "S", "P", "D", "L", "R"]


command = listeData.split(" ")
# command[1] = combien de caisse à bouger 
# command[3] = depuis
#  command[5] = vers
for i in range(int(command[1])):
    print(i)
    locals()["t"+command[5]].append(locals()["t"+str(command[3])][-int(command[1]) + i])
    del locals()["t"+command[3]][-int(command[1]) + i]

print("t4", t4 )
print("t8", t8 )