from os import system
letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',"1","2","3","4","5","6","7","8","9","0"," ","!","¡","¿","?","#","%","/","(",')',"-"]
letras_tras=['ñUdPg', 'cbfIs', '9dmWJ', '5lZMB', 'KufKT', '0ñpuF', 'JjXÑo', 'XeOM7', 'osh8G', 'UlA9e', 'ÑrNGX', '6RQJd', '9c0Cg', 'a4RlC', 'tp8MX', 'gGPVZ', 'dd3Q4', 'EbUÑN', 'FrDUY', '7uCCB', 'RiKt1', 'ZQzGF', 'ñqPtw', 'hHIyx', 'FZNR9', 's5YLo', '397QD', '0ek89', 'wk7Oi', 'UrU0J', 'D6DeU', 'ZkTt4', 'v8ELv', 'ByJnR', 'iFdjf', 'j7JzA', 'jP2nh', 'Bv50v', 'T1Wi4', 'Kyubñ', '5JqDS', 'dxz72', 'ucwJc', 'VQIHd', 'EUÑeA', 'Ya5lp', 'PRdÑw', 'pyaIx', 'hufgX', 'DyNJw', 'dPvzo', 'Pnut4', 'WQq6Ñ', '4XUWj', 'sgj88', 'SjtTd', 'UOPdC', 'tFñmx', 'kCKPX', 'kñ4TG', 'zsñI0', 'DP6qp', 'titA7', 'Mpcr4', 'Ldnkv', 'SRsñl', 'a54dN', 'eNCcU', 'Wwd54', 'U7OM2', '7h59u', 'ZJEMk', 'x1quA', 'SaGZp', 'H0JZS','   ']
codigo_s=[]
def validar_menu():
    while True:
        try:
            numero_ok=int(input())
            if numero_ok>3:
                while numero_ok>3:
                    system("cls")
                    print("numero no valido, ingrese del 1 al 3")
                    print("------------------")
                    print("1------traspasar-|")
                    print("2-----------info-|")
                    print("3----------salir-|")
                    print("------------------")
                    numero_ok=int(input())
            return numero_ok

        except ValueError:
            system("cls")
            print("error : letra detectada, ingrese un numero")     
            print("------------------")
            print("1------traspasar-|")
            print("2-----------info-|")
            print("3----------salir-|")
            print("------------------")    
def trasformador(palabra):
   palabra1=palabra
   codigo=str("")
   contador=len(palabra)
   contador2=(1)
   Npalabra=int(0)
   contadorcodigo=int(1)
   while contador2<=contador:
      codigo=codigo+palabra[Npalabra]
      if contadorcodigo==5:
         codigo_s.append(codigo)
         contadorcodigo=0
         codigo=""
      contadorcodigo=contadorcodigo+1   
      contador2=contador2+1
      Npalabra=Npalabra+1     
   return palabra1
def convertir():
    palabra=list(input())
    trasformador(palabra)
    palabra_trans=str("")
    contador1=len(palabra)
    contador2=int(1)
    Nletras=int(0)
    Npalabra=int(0)
    X=int(0)
    while contador2<=len(codigo_s):
        if Nletras>=75:
            Nletras=0
            Npalabra=0
            break
        if codigo_s[Npalabra]==letras_tras[Nletras]:
            palabra_trans=palabra_trans+letras[Nletras]
            Npalabra=Npalabra+1
            Nletras=0
            contador2=contador2+1
            X=1
        else:
            Nletras=Nletras+1  
    while contador2<=contador1:
        if X==1:
            break
        if palabra[Npalabra]==letras[Nletras]:
            palabra_trans=palabra_trans+letras_tras[Nletras]
            Nletras=0
            Npalabra=Npalabra+1
            contador2=contador2+1
        else:
            Nletras=Nletras+1   
    if X==1:       
        system("cls")             
        print("mensaje desencriptado :")         
        print("---",palabra_trans,"---")

    else:
        system("cls")             
        print("mensaje encriptado :")         
        print("---",palabra_trans,"---")
        palabra_trans=("")
    codigo_s.clear()


while True:
   print("-----------------")
   print("1------traspasar-|")
   print("2-----------info-|")
   print("3----------salir-|")
   print("-----------------")
   S=int(validar_menu())
   if S==1:
       system("cls")   
       print("ingresar mensaje:")
       convertir()   
   elif S==0:    
      print("letras",len(letras))   
      print("codigo:",len(letras_tras))   
   elif S==2:
      system("cls")
      print("caracteres disponibles :",len(letras_tras))
      print(letras)
      print("version: alfa 0.1.2")
   elif S==3:
      print("programa terminado")
      break 

