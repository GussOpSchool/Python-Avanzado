# Crear un directori dins /home/cicles/AO que es digui Prova, canviar-nos a aquest directori, a dins, crear el fitxer Ex12.txt i posar a dins el nom de tots els companys de classe.
# Tancar el fitxer. Obrir-lo per afegir el nom dels professors. Tancar-lo. Finalment, l’obrirem i posarem tot el seu contingut dins una llista de noms.

import os

companeros = ["Alejandro el Pequeño", "Gustavo el Tecchio", "Adolf Hitler", "Donkey Kong", "Bowser", "Hola el Mundo", "Jimmy Neutron"]
profesores = ["Joan Carreras", "Ayrton Senna", "Profesor Jirafales"]

os.makedirs("/home/cicles/AO/Prova", exist_ok = True)
os.chdir("/home/cicles/AO/Prova")

with open("Ex12.txt", "w") as archivotexto:
      archivotexto.write("- - - ALUMNOS - - -")
      for alumno in companeros:
            archivotexto.write("\n" + alumno)

with open("Ex12.txt", "a") as archivotexto:
      archivotexto.write(" \n \n- - - PROFESORES - - -")
      for profesor in profesores:
            archivotexto.write("\n" + profesor)

with open("Ex12.txt", "r") as archivotexto:
      listanombres = (archivotexto.read()).split("\n")
      listanombres.remove("- - - ALUMNOS - - -")
      listanombres.remove("- - - PROFESORES - - -")
      listanombres.remove(" ")

print(listanombres)