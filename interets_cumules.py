taux = float(input("Quel est le taux ? "))
capital = int(input("Capital de départ ? "))
nb_annees = int(input("Nombre d'années ? "))
interets_cumules = 0

for annee in range(1,nb_annees):
    interets = capital * taux
    capital = capital + interets
    interets_cumules = interets_cumules + interets
    print("Annee {} : interets = {} / capital = {}".format(annee, round(interets_cumules,2), round(capital,2)))

print("-------------------")
print("Les intérêts cumules sont de {}".format(round(interets_cumules,2)))
print("Le nouveau capital après {} années est de {}".format(nb_annees, round(capital,2)))