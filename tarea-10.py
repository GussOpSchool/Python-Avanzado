# Crear una funció que controli la divisió per zero i ens avisi que volem fer-ho.

def dividir(dividiendo, divisor):
      return dividiendo / divisor if divisor != 0 else print("El divisor es cero. Imposible dividirlo")

divid = int(input("Introduce el dividiendo: "))
divis = int(input("Introduce el divisor: "))
print(dividir(divid, divis) or "")