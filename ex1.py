def moyenne( a, b, c):
    return (a+b+c)/3

print("entrer les notes entre 0 et 20")
a= int(input("donner note1 "))
b= int(input("donner note2 "))
c= int(input("donner note3 "))
if(moyenne(a,b,c)>16):
    print("tres bien")
elif(14<=moyenne(a,b,c)):
    print("bien")
elif(12<=moyenne(a,b,c)):
    print("assez bien")
elif(10<=moyenne(a,b,c)):
    print("passable")
else:
    print("insuffisant")

print(moyenne(a,b,c))
