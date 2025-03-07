# Crear una llista dels 10 primers parells. Utilitzar list comprehensions. Ex: [2, 4, 6, 8, 10, 12, ...].

def listcomprehension():
      lista = [i for i in range(1, 21) if i % 2 == 0]
      print(lista)

listcomprehension()