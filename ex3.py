
def convertir_enseconde(secondes):
    heures=secondes//3600
    s_res=secondes%3600
    minutes=s_res//60
    secondes=s_res%60
    return heures,minutes,secondes

a=int(input("entrer un entier en secondes"))
heures, minutes, secondes = convertir_enseconde(a)
print(f"{a} secondes équivalent à {heures} heures, {minutes} minutes et {secondes} secondes.")

