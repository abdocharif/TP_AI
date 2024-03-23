def eqt(a,b,c):
   
    delta=b**2 - 4*a*c
    if(delta<0):
        print("pas de solution")
    elif(delta>0):
        x=(-b-sqrt(delta))/2*a
        y=(-b+sqrt(delta))/2*a
        print(x ,"and", y)
    else:
        z=-b/2*a
        print(z)
        print("anass")
a= int(input("donner a "))
b= int(input("donner b "))
c= int(input("donner c "))
eqt(a,b,c)