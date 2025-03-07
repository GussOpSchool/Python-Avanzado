# Crear una funció que permeti llegir la informació d’un fitxer, però que controli que el fitxer existeix i que la seva obertura no doni cap problema. Fes-ho també utilitzant with.
# Si voleu podeu practicar el try, except afegint-ho a les funcions anteriors.

def abrirtxt(archivo):
      try:
            fichero = open(archivo + ".txt")
            print(fichero.read())
      except:
            print("¡Error en abrir el archivo! Asegurate que este existe")

while True:
      elegido = input("Escribe el nombre del archivo que quieres leer (no hace falta poner '.txt'): ")
      abrirtxt(elegido)