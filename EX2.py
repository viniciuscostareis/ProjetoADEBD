numeros = []

for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

busca = int(input("\nDigite um número para buscar na lista: "))
if busca in numeros:
      posicoes = []
      for i in range(len(numeros)):
        if numeros[i] == busca:
            posicoes.append(i)
      print(f"\nO número {busca} foi encontrado nas posições: {posicoes}")
else:
      print(f"\nO número {busca} não está na lista.")

