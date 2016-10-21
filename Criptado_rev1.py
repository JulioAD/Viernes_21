# Criptado de palabras y desplazamiento posterior a la derecha
# Octubre 2016 RVIGO

# Solicita texto a codificar
def mensaje():
    return input('Introduce texto a codificar >>> ')

# Solicita clave para codificacion de texto
def codigo():
    while True:
        clave=int(input('Introduce parametro de cifrado (0>P>26) >>> '))
        if (0<= clave <=26):
            return clave
            
# Solicita parametro para desplazamiento de palabras a la derecha
def desplaza(texto):
    MAX_DESPLAZA=len(texto.split())
    while True:
        parametro=int(input('Introduce desplazamiento de palabras a la derecha (0>D>%s) >>> ' %(MAX_DESPLAZA-1)))        
        if (0<= parametro <=(MAX_DESPLAZA-1)):
            return parametro 
            
# Codifica texto con clave  
def criptado(texto, clave):         
    cadena_aux=''
    for letra in texto:
        if letra.isalpha():
            if letra.isupper():
                if (ord(letra)+clave)>ord('Z'):
                    cadena_aux += chr(ord(letra)+clave-26)                 
                else:
                    cadena_aux += chr(ord(letra)+clave)                   
            elif letra.islower():
                if (ord(letra)+clave)>ord('z'):
                    cadena_aux += chr(ord(letra)+clave-26)                   
                else:    
                    cadena_aux += chr(ord(letra)+clave)                
        else:
            cadena_aux += letra            
    return  cadena_aux   

# Desplaza palabras del codificado hacia dcha
def desplaza_palabras(texto_cifrado, parametro):
    cadena_aux=' '  
    lista_palabras=texto_cifrado.split()
    lista_aux=[]
# Inicializo lista_aux[] 
    for i in range(len(lista_palabras)):
        lista_aux.append('0')
# Rotacion de palabras    
    for i in range(len(lista_palabras)):
        if (i + parametro) <len(lista_palabras):
            lista_aux[i+parametro]=lista_palabras[i]
        else:
            lista_aux[i+parametro-(len(lista_palabras))]=lista_palabras[i]
    return cadena_aux.join(lista_aux)
         
# Ejecucion del programa
# Solicita texto a encriptar y clave            
texto= mensaje()
clave=codigo()

# Si hay varias palabras, solicita parametro de rotacion a derechas 
if len(texto.split())> 1:
     parametro=desplaza(texto)
     
# Ejecuta criptado     
texto_cifrado=criptado(texto,clave) 
print('\n Texto a cifrar: \n', texto)

# Si hay varias palabras, ejecuta rotacion a derechas
if len(texto.split())> 1:
    print('\n Texto cifrado: \n', desplaza_palabras(texto_cifrado,parametro))
else:
    print('\n Texto cifrado: \n', texto_cifrado) 
    
# Clase EOI    

 

    

