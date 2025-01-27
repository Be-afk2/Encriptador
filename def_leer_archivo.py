def leerarchivo():
    archivo=open(r"C:\Users\cleoe\Desktop\benja\encriptador\alfa 0.1.2\benja.txt","r")
    textodelarchivo=archivo.read()
    palabra=list(textodelarchivo)
    contador=len(palabra)
    contador2=int(1)
    Nletras=int(0)
    codigo=str("")
    NC=int(1)
    system("cls")
    while contador2<=contador:
        if NC>=5:
            codigo=codigo+(palabra[Nletras])
            Nletras=Nletras+1
            codigo_s.append(codigo)
            codigo=("")
            NC=1
            print(codigo_s)
            contador2=contador2+1
        if palabra[Nletras]==" ":
            Nletras=Nletras+1
            contador2=contador2+1
            NC=NC+1
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