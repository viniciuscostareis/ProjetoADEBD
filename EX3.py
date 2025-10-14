 numeros_novo = []

for i in range(10):
    numeroo = int(input("Digite um número: "))
    numeros_novo.append(numeroo)
 Vinicius: for i in range(len(numeros_novo)):
    if numeros_novo[i] < 0:
        numeros_novo[i] = 0

print("Lista após substituir negativos por 0:", numeros_novo)