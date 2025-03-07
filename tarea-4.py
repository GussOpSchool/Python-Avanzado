def concatenar(lista1, lista2):
      for i, j in zip(lista1, lista2):
            listatemp = []
            listatemp.extend([i, j])
            print("-".join(listatemp))

listaa = ["sub", "supra"]
listab = ["campeón", "campeona"]
concatenar(listaa, listab)
