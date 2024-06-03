n = int(input("saisir un nombre  "))
s=0
for i in range(1,n):
    if(n%i==0):
        s +=i
if s== n:
    print ("le nombre est parfait")
else:
    print ("le nombre est pas parfait ")
