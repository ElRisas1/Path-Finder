import hashlib
import json
import tkinter as tk
from tkinter import filedialog

numerito = 1
HashBuscado = ""
Longitud = ""


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
        return datos_json
        
    except FileNotFoundError:
        print(f"Error: El archivo no fue encontrado en la ruta '{ruta_archivo}'.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado durante la conversión: {e}")
        return None


def convertirAByte(valor):
    valor = valor.encode('utf-8')
    return valor
   
def EnCodeAndSearch():
    DatosContraseñas = json_resultante
    #Insertamos el Json de las contraseñas mas usadas que he hecho por aburrimiento extremo (hay algunos mejores)
    
    
   
    print("\n--- Comenzando las pruebas... ---")

    for clave, contraseña in DatosContraseñas.items():
        global HashBuscado
        global numerito

        PassHash = hashlib.sha256()
        PassHash.update(convertirAByte(contraseña))
        PassHash = PassHash.hexdigest()
        if PassHash == HashBuscado:
            print(f"\n---Intento {numerito}: ¡¡Contraseña descubierta!!, La contraseña es: {contraseña}, el Hash Coincide---")
            break
        else:
            #print(f"intento {numerito}: No hay coincidencia")
            numerito = numerito + 1
        #numerito= numerito + 1
        
       

"""
Ahora empieza el flujo principal
"""
print("              \n💀 Bienvenido al Password Finder 💀\n \nEste programa revisa si el hash que has introducido coicide con el Hash de alguna contraseña que existe en la base de datos del programa")
HashBuscado = str(input("Por favor introduce el Hash que quieres revisar: "))
Longitud = str(len(HashBuscado))
while Longitud != "64":
    HashBuscado = str(input("El contenido introducido no es un hash, por favor intentalo de nuevo: "))
    Longitud = str(len(HashBuscado))

print("Hash Correcto")
nada =  input("Ahora dale al enter para introducir el diccionario formato .txt que quieres usar: ")
ruta_seleccionada = solicitar_ubicacion_archivo()
# 2. Realizar la conversión
json_resultante = convertir_txt_a_json_indexado(ruta_seleccionada)

parada1 = input("pulsa para seguir...")
EnCodeAndSearch()


print ("\nFinal de programa")