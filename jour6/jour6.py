f = open("jour6/data6.txt", "r")
longueLigne = f.read()
maxlLength = len(longueLigne)

i=14
while i < maxlLength:
    if len(set(longueLigne[i-14:i])) == 14 :
        break
    else:
        i += 1
print(" La réponse de l'exercice 1 est", i)

