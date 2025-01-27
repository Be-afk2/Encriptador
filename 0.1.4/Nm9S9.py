from os import system
import pathlib
from pathlib import Path
from os import mkdir
from datetime import datetime
ubicacion=str(pathlib.Path(__file__).parent.absolute())
letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',"1","2","3","4","5","6","7","8","9","0"," ","!","¡","¿","?","#","%","/","(",')',"-",":"]
letras_tras=['ñUdPg', 'cbfIs', '9dmWJ', '5lZMB', 'KufKT', '0ñpuF', 'JjXÑo', 'XeOM7', 'osh8G', 'UlA9e', 'ÑrNGX', '6RQJd', '9c0Cg', 'a4RlC', 'tp8MX', 'gGPVZ', 'dd3Q4', 'EbUÑN', 'FrDUY', '7uCCB', 'RiKt1', 'ZQzGF', 'ñqPtw', 'hHIyx', 'FZNR9', 's5YLo', '397QD', '0ek89', 'wk7Oi', 'UrU0J', 'D6DeU', 'ZkTt4', 'v8ELv', 'ByJnR', 'iFdjf', 'j7JzA', 'jP2nh', 'Bv50v', 'T1Wi4', 'Kyubñ', '5JqDS', 'dxz72', 'ucwJc', 'VQIHd', 'EUÑeA', 'Ya5lp', 'PRdÑw', 'pyaIx', 'hufgX', 'DyNJw', 'dPvzo', 'Pnut4', 'WQq6Ñ', '4XUWj', 'sgj88', 'SjtTd', 'UOPdC', 'tFñmx', 'kCKPX', 'kñ4TG', 'zsñI0', 'DP6qp', 'titA7', 'Mpcr4', 'Ldnkv', 'SRsñl', 'a54dN', 'eNCcU', 'Wwd54', 'U7OM2', '7h59u', 'ZJEMk', 'x1quA', 'SaGZp', 'H0JZS','KÑhXH',' ']
codigo_s=[]
now = datetime.now()
format=now.strftime("%d"+"/%m"+"/%Y"+"(%H"+":"+"%M)")
def validar_menu():
    while True:
        try:
            numero_ok=int(input())
            if numero_ok>5:
                while numero_ok>5:
                    system("cls")
                    print("numero no valido, ingrese del 1 al 5")
                    print("------------------")
                    print("1------traspasar-|")
                    print("2------leer_arch-|")
                    print("3-----------info-|")
                    print("4---validar_arch.|")
                    print("5----------salir-|")
                    print("------------------")
                    numero_ok=int(input())
            return numero_ok

        except ValueError:
            system("cls")
            print("error : letra detectada, ingrese un numero")     
            print("------------------")
            print("1------traspasar-|")
            print("2------leer_arch-|")
            print("3-----------info-|")
            print("4---validar_arch.|")
            print("5----------salir-|")
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
def convertir(format):
    palabra=list(input())
    trasformador(palabra)
    palabra_trans=str("")
    contador1=len(palabra)
    contador2=int(1)
    Nletras=int(0)
    Npalabra=int(0)
    X=int(0)
    while contador2<=len(codigo_s):
        if Nletras>=76:
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
        #TEXTO C       
        system("cls")             
        print("mensaje desencriptado :")         
        print("---",palabra_trans,"---")
        archivoC=open(ubicacion+"\carpeta"+"\historialC.txt","a")
        palabra2="".join(palabra)
        archivoC.write(palabra2+"   ")
        archivoC.close
        palabra_trans=("")

    #textoL
    else:
        system("cls")             
        print("mensaje encriptado :")         
        print("---",palabra_trans,"---")
        archivoL=open(ubicacion+"\carpeta"+"\historialL.txt","a")
        archivoL.write(palabra_trans+"   ")
        archivoL.close
        palabra_trans=("")
    codigo_s.clear()
def comprobar_carpeta(ubicacion):
    system("cls")   
    if Path(ubicacion+"\carpeta").exists()==True:
        print("carpeta ya creada ")
    else:
        print("archivos creados")   
        mkdir(ubicacion+"\carpeta")
    if Path(ubicacion+"\carpeta"+"\historialC.txt").exists()==True:
        print("txtC ya creado")
    else:     
        archivo=open(ubicacion+"\carpeta"+"\historialC.txt","w")
        print("txtC creado")
        archivo.close()
    if Path(ubicacion+"\carpeta"+"\historialL.txt").exists()==True:
        print("txtL ya creado")
    else:     
        archivo=open(ubicacion+"\carpeta"+"\historialL.txt","w")
        print("txtL creado")
        archivo.close()    
def leerarchivo(OM2,ubicacion):
    if OM2==1:
        archivo=open(ubicacion+"\carpeta"+"\historialL.txt","r")
        palabra=list(archivo.read())
        archivo.close()
        contador=len(palabra)
        contador2=int(1)
        Nletras=int(0)
        codigo=str("")
        NC=int(1)
        #aqui solo esta pasando lo del txt a una lista para recien trasformalo
        while contador2<=contador:
            if NC>=5:
                codigo=codigo+(palabra[Nletras])
                Nletras=Nletras+1
                codigo_s.append(codigo)
                codigo=("")
                NC=1   
                contador2=contador2+1
            if palabra[Nletras]==" ":
                Nletras=Nletras+1
                contador2=contador2+1
                codigo_s.append(" ")
            else:    
                codigo=codigo+(palabra[Nletras])
                NC=NC+1
                Nletras=Nletras+1
                contador2=contador2+1
        palabra_tras=str("")
        contador=len(codigo_s)
        contador2=int(1)
        Nletras=int(0)
        Npalabra=int(0)
        contador_espacios=int(0)
        while contador2<=contador:
            if codigo_s[Npalabra]==" ":
                contador_espacios=contador_espacios+1
                Npalabra=Npalabra+1
                contador2=contador2+1
                if contador_espacios>=3:
                    palabra_tras=palabra_tras+"\n"
                    contador2=contador2+1
            else:

                if codigo_s[Npalabra]==letras_tras[Nletras]:
                    palabra_tras=palabra_tras+letras[Nletras]
                    Npalabra=Npalabra+1
                    contador2=contador2+1
                    Nletras=0
                else:
                    Nletras=Nletras+1
        codigo_s.clear()                
    elif OM2==2:
        trasformador(palabra)
        contador

    else:
        print("opcion ingresada no valida")                       
    system("cls")
    print("----------texto_L---------------")   
    print(palabra_tras) 
    codigo_s.clear()        
    
while True:
    print("-----------------")
    print("1------traspasar-|")
    print("2------leer_arch-|")
    print("3-----------info-|")
    print("4---validar_arch.|")
    print("5----------salir-|")
    print("-----------------")
    S=int(validar_menu())
    if S==1:
        system("cls")   
        print("ingresar mensaje:")
        convertir(format)   
    elif S==2:
        print("1--------L")
        print("2--------C")
        OM2=int(input("..."))
        leerarchivo(OM2,ubicacion)
    elif S==3:
        system("cls")
        print("caracteres disponibles :",len(letras_tras))
        print(letras)
        print("version: alfa 0.1.4")
        print("ubicacion carpeta" + ubicacion+"\carpeta")
        print("ubicacion archC.txt" + ubicacion+"\carpeta"+"\historialC")
        print("ubicacion archl.txt" + ubicacion+"\carpeta"+"\historialL")
    elif S==4:
        comprobar_carpeta(ubicacion)     
    elif S==5:
        system("cls")  
        print("programa terminado")
        break

    elif S==0:    
        print("letras",len(letras))   
        print("codigo:",len(letras_tras))      