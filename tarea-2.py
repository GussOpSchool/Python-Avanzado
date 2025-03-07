from functools import reduce

def Pasaranumero(lista):
      listab = map(str, lista)
      print(reduce(lambda x, y: str(x) + str(y), listab))

a = [3, 4, 1, 5]
Pasaranumero(a)