# Ejemplo de uso de listas
Frutas=["apple", "banana", "cherry"]
misNumeros=[111, 222, 333]

print(Frutas)

print(misNumeros)

print("--Accediendo a los elementos de la lista--")

print(Frutas[-2])

if "a+" in Frutas:
  print("Yes, 'apple' is in the fruits list")
else:
  print("no")

print("Numero de frutas")
Nfrutas=len(Frutas)
print(f"Numero de frutas {Nfrutas}")

print("Ciclo for en lista")

posicion=0
for naranja in Frutas:
  print(posicion, " ", naranja)
  posicion=posicion+1