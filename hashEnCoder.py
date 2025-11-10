import hashlib


porsiacaso = True

while porsiacaso:
    preguntita =input("Tipo de Hash que quieres? \n[1] SHA256\n[2] SHA512\n")
    if preguntita == "1":
        print("Hash seleccionado SHA256")
        bolso = hashlib.sha256()
        break
    elif preguntita == "2":
        print("Hash seleccionado SHA512")
        bolso = hashlib.sha512()
        break

    print("tonto intentalo de nuevo")

print("Todo correcto sacando hash...")

cosa = input("introduce la palabra o contraseña que quieras transformar:\n")
cosa = cosa.encode('utf-8')

bolso.update(cosa)
bolso = bolso.hexdigest()
print ("item: " + bolso)
cantidad_caracteres = str(len(bolso))
print("cantidad: " + cantidad_caracteres)