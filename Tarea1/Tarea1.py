import numpy as np

print("Ingrese los elementos de la matriz 2x2:")

matriz = []
for i in range(2):
    fila = []
    for j in range(2):
        valor = int(input(f"Ingrese el valor en la posición en la matriz ({i+1},{j+1}): "))
        fila.append(valor)
    matriz.append(fila)


matriz = np.array(matriz)


Mtranspuesta = matriz.T


print("\nMatriz Normal:")
print(matriz)

print("\nMatriz Transpuesta:")
print(Mtranspuesta)

