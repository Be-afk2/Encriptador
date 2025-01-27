import random
letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',"1","2","3","4","5","6","7","8","9","0","!","¡","¿","?","#","%","/","(",')',"-"]
letras_tras=[]
x=int(1)
z=int(0)
print("hay ",len(letras)," caracteres")
zx=str("")
print("TOTAL CARACTERES :",len(letras))
caracteres=int(1)
contador=int(0)
#print(len(letras))
while caracteres<=76:
   x=1    
   while x<=5:
      z=random.randint(0,63)
      xz=letras[z]
      zx=zx+xz
      x=x+1
   letras_tras.append(zx)
   contador=contador+1
   zx=("")  
   caracteres=caracteres+1 
print("se generaron",contador," instancias")

print("--------------------------------------")
print(letras)
print(letras_tras)