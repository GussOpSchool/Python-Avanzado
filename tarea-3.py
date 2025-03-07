def comienzapor(palabras, letra):
      print("Las palabras que empiezan por {} son {}".format(letra, list(filter(lambda x: x[0] == letra.lower(), palabras))))

listapalabras = ["gustavo", "alejandro", "escuela", "talk", "tuah", "propiedad", "en", "egipto"]
entradaletra = input("Cual letra quieres filtrar?: ")
comienzapor(listapalabras, entradaletra)