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
        title="Select the text file (.txt) for indexed conversion",
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
        print("Operation cancelled, no file was selected")
        return None

    try:
        print(f"\n--- Reading and converting the file: {ruta_archivo} ---")
        
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            indice = 1
            for linea in archivo:
                contenido_limpio = linea.strip()
                if contenido_limpio:
                    datos_json[str(indice)] = contenido_limpio
                    indice += 1
                
        
        print("---------------------------------------")
        print("✅ Password file uploaded successfully.")
        # 2. DEVOLVER el objeto Python de tipo diccionario (dict)
        #print(f"BALIZA 1 {datos_json}")
        return datos_json
    
        
    except FileNotFoundError:
        print(f"Error: the file was not found in the path'{ruta_archivo}'.")
        return None
    except Exception as e:
        print(f"An unexpected error ocurred during the conversion: {e}")
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
   
    print("\n--- Starting the testing... ---")
    numerito = 0
    encontrado = False
    


    for clave, contraseña in json_resultante.items():

        if Longitud =="64":PassHash = hashlib.sha256()
        elif Longitud =="128":PassHash = hashlib.sha512()

        PassHash.update(convertirAByte(contraseña))
        PassHash = PassHash.hexdigest()
        if PassHash == HashBuscado:
            print(f"\n---Try {numerito}: ¡¡Password found!!, the password is: \33[31m{contraseña}\033[0m, the Hash matches---")
            print(f"----------------\nYou have entered---> {HashBuscado}\nHash found----> {PassHash}\n----------------")
            encontrado = True
            break
        else:
            #print(f"intento {numerito}: No hay coincidencia") ADVICE you can put this in the code if u want to print all not matched trys. Its actually 
            numerito = numerito + 1
        #print(f"BALIZA 6 para ver si hay passhash {PassHash}")
        #numerito= numerito + 1
        
#Función que llama a solicitar_ubi y que es usada una vez por vuelta O no depende 
#de si quiere mantener el mismo diccionario o cambiarlo, como se usa puntualmente la saqué fuera por comodidad
def seleccionDeDiccionario():
    global json_resultante

    nada =  input("Now press Intro key to enter the .txt format dictionary you whis to use: ")
    ruta_seleccionada = solicitar_ubicacion_archivo()
    # 2. Realizar la conversión
    #print(f"BALIZA 2 {json_resultante}")
    json_resultante = convertir_txt_a_json_indexado(ruta_seleccionada)
    #print(f"BALIZA 3 despues de rellenar {json_resultante}")
    parada1 = input("Press Enter to start the search...")


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
    global encontrado

    #------------------------------

    HashBuscado = str(input("Please enter the hash you want to check(SHA256 o SHA512): "))
    Longitud = str(len(HashBuscado))

    while Longitud != "64" and Longitud != "128":
        HashBuscado = str(input("The content entered is not a Hash (Only SHA256 or SHA512), please try again: "))
        Longitud = str(len(HashBuscado))
    if Longitud=="64":print("Hash SHA256 correct")
    elif Longitud=="128":print("Hash SHA512 correct")

    if repitiendo == True:
        if not json_resultante:
            seleccionDeDiccionario()
        else:
            pregunta2 = input("Do you want to use the dictionary that's already loaded?(Y/n)")
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
    
    if encontrado == False:
        print(f"\n{numerito} tests have been performed, but \33[31mno matches\033[0m were found, try another dictionary.")
    

    pregunta1 = input("Do you want to continue testing?(Y/n)\n")
    if pregunta1.upper()[0] == "Y":
        repitiendo = True
        ejecutar = True
    else:
        ejecutar = False


print("\n\033[32m 💀 WELCOME TO PATH FINDER 💀")
print("\n\33[0m This program automatically checks if the hash you are about to enter matches the hash of any password in the txt dictionary you enter to find out the password\n Version 1.1en\n Made by joseludev\n")

while ejecutar == True:
    BuclePrincipal()

print("Thanks using the \033[32m PATH FINDER\033[0m\nEnd program")
salir = input("Press Enter to exit...")