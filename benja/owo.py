from os import system
letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',"1","2","3","4","5","6","7","8","9","0"," "]
letras_tras=['CovsJ', 'IcACl', 'EAkon', 'ETñtÑ', 'HYGv6', 'DLhQX', 'RRbxr', 'Sn7IN', 'vY8PÑ', '3FUcK', '3DU4D', 'Ñ7q6v', '2LHU5', 'qoUhs', '57rcd', 'SbFdN', 'OñVVD', 'Pgqz4', 'ZHOr5', 'Dvexs', 'Vj47G', 'YPwAi', '68y3l', 'QFjl5', 'P5hAI', 'MzoeH', 'DPPOq', 'lP8nm', 'OjSoK', 'Uvxuo', 'IZsaC', 'SygaB', '788tK', '34EaK', 'xFDC1', 'ñnvim', 'rLyUx', 'qyhiV', '778su', 'byEBw', 'zoAñ2', '7Y8lM', '8fjuF', 'oBbxj', 'MhQA6', 'A4ENF', 'eILLa', 'YTÑRx', 'CRvNl', 'oCHñG', '2mqcR', 'KIGwa', 'wLñw5', '3oSñp', 'layvL', 'ucÑQÑ', '3Xs5W', 'lRQfL', 'a5FGA', 'jxiOc', 'CukSj', 'VARWS', 'cW5T3', 'ENyiS', '6qLFK']
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
            print("error : letra detectada, ingrese un numero")
def encriptar():
   palabra=list(input())
   palabra_tras=str("")
   contador=len(palabra)
   contador2=int(1)
   Nletras=int(0)
   Npalabra=int(0)
   while contador2<=contador:
      if palabra[Npalabra]==letras[Nletras]:
         palabra_tras=palabra_tras+letras_tras[Nletras]
         contador2=contador2+1
         Npalabra=Npalabra+1
         Nletras=0
      else:
         Nletras=Nletras+1
   system("cls")
   print("mensaje encriptado :")         
   print("---",palabra_tras,"---")          
def trasformador():
   palabra=list(input())
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
def desencriptar():
   palabra_tras=str("")
   contador=len(codigo_s)
   contador2=int(1)
   Nletras=int(0)
   Npalabra=int(0)
   while contador2<=contador:
      if codigo_s[Npalabra]==letras_tras[Nletras]:
         palabra_tras=palabra_tras+letras[Nletras]
         Npalabra=Npalabra+1
         contador2=contador2+1
         Nletras=0
      else:
         Nletras=Nletras+1
   system("cls")
   print("mensaje desencriptado")         
   print("---",palabra_tras,"---") 
   codigo_s.clear()
while True:

   print("-----------------")
   print("1------encriptar-|")
   print("2---desencriptar-|")
   print("3----------info-|")
   print("4----------salir-|")
   print("-----------------")
   S=validar_menu()
   if S==1:   
      system("cls")
      print("ingresar mensaje:")
      encriptar()
   elif S==2:
      trasformador() 
      print("--------------")
      print("mensaje desencriptado:")   
      desencriptar()
   elif S==5:    
      print("letras",len(letras))   
      print("codigo:",len(letras_tras))   
   elif S==3:
      system("cls")
      print("disponibles :")
      print(letras)
      print("version: alfa 0.3")
   elif S==4:
      break 