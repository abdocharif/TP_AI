def Trie(tab):
    for i in range(len(tab) - 1):
        if tab[i] > tab[i + 1]:
            return False
    return True

Tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
if Trie(Tab):
    print("Le tableau est trié ")
else:
    print("Le tableau n'est pas trié ")
