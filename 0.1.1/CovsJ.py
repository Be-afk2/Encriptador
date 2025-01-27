from os import system
letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',"1","2","3","4","5","6","7","8","9","0"," ","!","¡","¿","?","#","%","/","(",')',"-"]
letras_tras=['Nm9S9', 'rB36c', 'UWnXj', 'hlpB0', 'yzN76', 'Uunen', 'BDcpz', 'T0xGb', '5x9Qw', 'kpWQk', 'plz5y', 'T14DO', 'AjMAL', 'LcOGN', 'Nt11B', '8ovrt', '4jrY!', 'MX5Mo', 'e5l9c', 'pfUC8', 'KxrñP', 'PgejM', 'pArot', 'VaPPv', 'waOoV', 'QIh6p', 'qwD!S', 'iboE4', 'nGRUR', 'PWTAT', 'mbñÑ!', 'ZHkfD', '1Nk!X', 'fKxu8', '!w19e', 'ZfnPL', 'Xmm6L', '!HJkX', 'sHBMG', '1wq9M', 'nyFzP', 'stA4N', 'LHuvp', 'pCAko', 'GUsxK', 'x06r1', 'opZsf', 'BM7Ah', 'omKyN', 'sSfNm', 'CO4iZ', 'sQ7e5', 'Yy6L3', 'D1cy7', 'YpB35', 'NAcbA', '5qPq2', 'CHLg1', 'AkfAv', 'kbÑÑe', 'RZMVA', 'l9Zñz', '8eJ70', 'E3IJ!', 'w6WrB', 'rZEfJ', 'Tjhln', 'bX07r', 'y6YkK', 'RMk0o', 'd2VEM', 'Ñk59w', 'agRLj', 'Hgqht', '4U7ÑU']
codigo_s=[]
def validar_menu():
    while True:
        try:
            numero_ok=int(input())
            if numero_ok>4:
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
      print("version: alfa 0.1.1")
   elif S==3:
      break 