
sexe=str(input("entrer le sexe "))
age=int(input("entrer l'age"))
if(age>20 and sexe=="homme"):
        print("il faut payer l'impot ")
elif(18<age<35 and sexe=="femme"):
        print("il faut payer l'impot ")
else:
        print("il ne faut pas payer l'impot ")
    