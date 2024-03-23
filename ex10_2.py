def produit_scalaire(a, b):
    if len(a) != len(b):
        return "Les vecteurs doivent avoir la même taille"
    produit = 0
    for i in range(len(a)):
        produit += a[i] * b[i]
    return produit
a = [2, 5, 3]
b = [7, 1, 0]
resultat = produit_scalaire(a, b)
print("Le produit scalaire de a et b est ", resultat)
