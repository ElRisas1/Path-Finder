import hashlib
import json
import tkinter as tk
from tkinter import filedialog


#------VARIABLES GLOBALES-----
numerito = 1
HashBuscado = ""
Longitud = ""
encontrado = False
ejecutar = True
repitiendo = False
json_resultante = {}

#--------------------------------

#Selección de archivo .txt y guardado en una variable global
def solicitar_ubicacion_archivo():
    """Abre el explorador de archivos y devuelve la ruta seleccionada."""
    root = tk.Tk()
    root.withdraw()
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona el archivo de texto (.txt) para conversión Indexada",
        filetypes=(("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    return ruta_archivo

# --- La Función de Conversión a JSON (Indexada) ---
def convertir_txt_a_json_indexado(ruta_archivo):
    """
    Lee un archivo de texto, asigna un índice numérico consecutivo (empezando en 1) 
    a cada línea no vacía, y lo convierte a un objeto JSON.
    """
    datos_json = {}
    
    if not ruta_archivo:
        print("Operación cancelada. No se seleccionó ningún archivo.")
        return None

    try:
        print(f"\n--- Leyendo y convirtiendo el archivo: {ruta_archivo} ---")
        
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            indice = 1
            for linea in archivo:
                contenido_limpio = linea.strip()
                if contenido_limpio:
                    datos_json[str(indice)] = contenido_limpio
                    indice += 1
                
        
        print("---------------------------------------")
        print("✅ Archivo de contraseñas cargado correctamente.")
        # 2. DEVOLVER el objeto Python de tipo diccionario (dict)
        #print(f"BALIZA 1 {datos_json}")
        return datos_json
    
        
    except FileNotFoundError:
        print(f"Error: El archivo no fue encontrado en la ruta '{ruta_archivo}'.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado durante la conversión: {e}")
        return None

#sencilla funcion de convertir a byte la contraseña, ya que se usa todo el rato la saque fuera por comodidad
def convertirAByte(valor):
    valor = valor.encode('utf-8')
    return valor
   
#Función de codificar y probar hashes
def EnCodeAndSearch():
    
    #Insertamos el Json de las contraseñas mas usadas que he hecho por aburrimiento extremo (hay algunos mejores)
    global json_resultante
    global HashBuscado
    global numerito 
    global encontrado
    global Longitud


    #print(f"BALIZA 4 antes de codificar {json_resultante}")
   
    print("\n--- Comenzando las pruebas... ---")
    numerito = 0
    


    for clave, contraseña in json_resultante.items():

        if Longitud =="64":PassHash = hashlib.sha256()
        elif Longitud =="128":PassHash = hashlib.sha512()

        PassHash.update(convertirAByte(contraseña))
        PassHash = PassHash.hexdigest()
        if PassHash == HashBuscado:
            print(f"\n---Intento {numerito}: ¡¡Contraseña descubierta!!, La contraseña es: \33[31m{contraseña}\033[0m, el Hash Coincide---")
            print(f"----------------\nHash introducido---> {HashBuscado}\nHash encontrado----> {PassHash}\n----------------")
            encontrado = True
            break
        else:
            #print(f"intento {numerito}: No hay coincidencia")
            numerito = numerito + 1
        #print(f"BALIZA 6 para ver si hay passhash {PassHash}")
        #numerito= numerito + 1
        
#Función que llama a solicitar_ubi y que es usada una vez por vuelta O no depende 
#de si quiere mantener el mismo diccionario o cambiarlo, como se usa puntualmente la saqué fuera por comodidad
def seleccionDeDiccionario():
    global json_resultante

    nada =  input("Ahora dale al enter para introducir el diccionario formato .txt que quieres usar: ")
    ruta_seleccionada = solicitar_ubicacion_archivo()
    # 2. Realizar la conversión
    #print(f"BALIZA 2 {json_resultante}")
    json_resultante = convertir_txt_a_json_indexado(ruta_seleccionada)
    #print(f"BALIZA 3 despues de rellenar {json_resultante}")
    parada1 = input("Pulsa enter para empezar...")


def BuclePrincipal():

    """
    Ahora empieza el flujo principal
    """
    #Declaracion Variables Globales
    global pregunta1
    global ejecutar
    global json_resultante
    global repitiendo
    global HashBuscado
    global Longitud

    #------------------------------

    HashBuscado = str(input("Por favor introduce el Hash que quieres revisar(SHA256 o SHA512): "))
    Longitud = str(len(HashBuscado))

    while Longitud != "64" and Longitud != "128":
        HashBuscado = str(input("El contenido introducido no es un hash, por favor intentalo de nuevo: "))
        Longitud = str(len(HashBuscado))
    if Longitud=="64":print("Hash SHA256 correcto")
    elif Longitud=="128":print("Hash SHA512 correcto")

    if repitiendo == True:
        if not json_resultante:
            seleccionDeDiccionario()
        else:
            pregunta2 = input("¿Quieres usar el diccionario que ya esta cargado?(Y/N)")
            if pregunta2.upper()[0] == "Y":
                EnCodeAndSearch()
            else:
                #Si no quiere usar el mismo diccionario le solicitamos que escoja uno nuevo
                seleccionDeDiccionario()
                #Y despues corremos el codigo de buscar
                EnCodeAndSearch()
    else:
        #Si no quiere usar el mismo diccionario le solicitamos que escoja uno nuevo
        seleccionDeDiccionario()
        #Y despues corremos el codigo de buscar
        EnCodeAndSearch()

   # EnCodeAndSearch()
    
    if encontrado == False:
        print(f"\nSe han realizado {numerito} pruebas, pero \33[31mno se han encontrado coincidencias\033[0m, prueba con otro diccionario")
    

    pregunta1 = input("¿Quieres seguir haciendo pruebas? (Y/N)\n")
    if pregunta1.upper()[0] == "Y":
        repitiendo = True
        ejecutar = True
    else:
        ejecutar = False


print("\n\033[32m 💀 BIENVENIDO AL PATH FINDER 💀")
print("\n\33[0m Este programa revisa automaticamente si el Hash que vas a introducir coicide con el Hash de alguna contraseña\n que este en el archivo txt que introduzcas, para conseguir averiguar la contraseña.\n Version 1.1es\nMade by joseludev")

while ejecutar == True:
    BuclePrincipal()

print("Gracias por usar el\033[32m PATH FINDER\033[0m\nFin de programa")
salir = input("Pulsa enter para salir...")