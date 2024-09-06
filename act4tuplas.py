arcoiris=("Azul", "Verde", "Rojo", "Amarillo")
print(arcoiris)
print("--Longitud arcoiris--")
print(len(arcoiris))

print("")

animales=("Panteras", 20, "Estatura", 1.7)
print(animales)
print("Elementos de las tuplas")
print(animales[2])

print("")

rateros = ("Juan", "Ana", "Pedro")
y = list(rateros)
y[0] = "Polainas"
x = tuple(y)

print(x)

print("")

print("Agregamos elementos")
Nanimal=("Boby", "Chetos")
y = list(Nanimal)
print(y)
y.append("Tontolin")
otratupla = tuple(y)

print(otratupla)

print("Uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)