from fractran import Fraction, Facteur, Fractran


#Calcul des sommes

somme = [Fraction(3, 2)]
facteurs_somme = Facteur([2, 3, 5])

for i in range(1, 11):
    for j in range(1, 11):
        resultat = Fractran(somme).run(facteurs_somme.nombre([i, j]))
        somme_i_j = facteurs_somme.décomposition(resultat)
        #print(f"{i} + {j} = {somme_i_j[1]}")


#Calcul des produits

produit = [Fraction(455, 33), Fraction(11, 13), Fraction(1, 11), Fraction(3, 7), Fraction(11, 2), Fraction(1, 3)]
facteurs_produit = Facteur([2, 3, 5, 7, 11, 13])

for i in range(1, 11):
    for j in range(1, 11):
        resultat = Fractran(produit).run(facteurs_produit.nombre([i, j, 0, 0, 0, 0]))
        produit_i_j = facteurs_produit.décomposition(resultat)
        print(f"{i} * {j} = {produit_i_j[2]}")


#Suite de Fibonacci

print("Fibonacci rend les couples (F(n), F(n+1)) :")
fibonacci = [Fraction(23, 95), Fraction(57, 23), Fraction(17, 39), Fraction(130, 17), Fraction(11, 14),     #suite de fractions formant le programme Fractran
          Fraction(35, 11), Fraction(19, 13), Fraction(1, 19), Fraction(35, 2), Fraction(13, 7), 
          Fraction(7, 1)]

sortie_brute = Fractran(fibonacci).suite(3, 1000)   #on calcule la suite de len 1000 de nombre généré par le programme en commençant par 3
sortie = [] 
for n in sortie_brute:
    if n == Facteur([2, 3]).nombre(Facteur([2, 3]).décomposition(n)):
        sortie.append(Facteur([2, 3]).décomposition(n))

print(sortie)


#Nombres premiers  

print("Voici les nombres premiers générés par les 100000 premiers termes de la suite :")
premiers = [Fraction(17, 91), Fraction(78, 85), Fraction(19, 51), Fraction(23, 38), Fraction(29, 33), Fraction(77, 29), Fraction(95, 23), Fraction(77, 19), Fraction(1, 17), Fraction(11, 13), Fraction(13, 11), Fraction(15, 14), Fraction(15, 2), Fraction(55, 1)]

sortie_brute = Fractran(premiers).suite(2, 100000)
sortie = []
for n in sortie_brute:
    if n == Facteur([2]).nombre(Facteur([2]).décomposition(n)):
        sortie.append(Facteur([2]).décomposition(n)[0])

print(sortie)
