achatMaison = 47262 # au 29/10/2020
relever2021 = 49115 # relever de compteur le 1/11/2021
estimer2021 = 47264
diff = relever2021 - estimer2021
telerelever = 1829
totalConsoM3 = diff + telerelever

print("\n \n \n \n consomation total en m3", totalConsoM3)
coeffDeConversion = 11.15
conversion = totalConsoM3 * coeffDeConversion

print("\n consomation total en kwH", conversion)

prixKwh = 0.05276

prixHt = conversion * prixKwh
print("\n Le prix Hors taxe revient a ", prixHt, "\n ")

TVA = 20
prixTVA = prixHt * TVA /100

print("\n La TVA coute", prixTVA, "\n ")

prixTtc = prixHt + prixTVA

print("\n La facture devrait couter ", prixTtc, "\n ")

