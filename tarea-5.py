def listaparadicc(lista):
      dicc = {}

      for i, e in enumerate(lista):
            dicc[e] = i
      return dicc

entralista = ["casa", "coche", "silla", "mesa"]
dicc = listaparadicc(entralista)
print(dicc)