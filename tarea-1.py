def lenp(frase):
      frase = frase.split(" ")

      longitud = list(map(len, frase))

      for i, j in zip(frase, longitud):
            print("La longitud de la palabra '{}' es de '{}' caracteres".format(i, j))

entrada = input("Escribe un frase y te devolveré la longitud para cada una de ellas: ")

lenp(entrada)