def calcul():
    n1=int(input("entrer entier 1"))
    n2=int(input("entrer entier 2"))
    opt=str(input("entrer opt"))
    if(opt=="+"):
        return n1+n2
    elif(opt=="-"):
        return n1-n2
    elif(opt=="*"):
        return n1*n2
    else:
        return n1//n2
print(calcul())